import requests
from bs4 import BeautifulSoup
import json
import re
import urllib
import os
from selenium import webdriver
from time import sleep


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 6.1; WOW64)',
        'Referer': 'http://music.163.com',
        'Host': 'music.163.com'
    }

    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print('request error')
        pass


def get_singer_info(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('ul', class_='f-hide').find_all('a')
    song_IDs = []
    song_names = []
    # print(links)
    for link in links:
        song_ID = link.get('href').split('=')[-1]
        song_name = link.get_text()
        # print(song_name)
        # print(song_ID)
        song_IDs.append(song_ID)
        song_names.append(song_name)
    return zip(song_names, song_IDs)


def get_lyric(song_id):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    html = get_html(url)
    json_obj = json.loads(html)
    initial_lyric = json_obj['lrc']['lyric']
    # print(lyric)
    regex = re.compile(r'\[.*\]')
    final_lyric = re.sub(regex, '', initial_lyric).strip()
    return final_lyric


def write_lyric(song_name, lyric):
    print('正在写入歌曲：{}'.format(song_name))
    with open('E:\\TXT\\{}.txt'.format(song_name), 'a', encoding='utf-8') as fp:
        fp.write(lyric)


def download_song(song_name, song_id):
    sinnger_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    print('正在下载歌曲：{}'.format(song_name))
    urllib.request.urlretrieve(sinnger_url, f'E:\\MP3\\{song_name}.mp3')


if __name__ == '__main__':
    singer_id = input('请输入歌手ID：')
    start_url = 'http://music.163.com/artist?id={}'.format(singer_id)
    html = get_html(start_url)
    # print(html)
    # with open('test.html', 'w', encoding='utf-8') as f:
    #     f.write(html)
    # with open('test.txt', 'r', encoding='utf-8') as f:
    #     html = f.read()
    # print(html)
    # path = r'E:\PycharmProject\MyProject\venv\Scripts\chromedriver.exe'
    # drive = webdriver.Chrome(executable_path=path)
    # drive.get('http://www.baidu.com')
    # sleep(5)

    get_singer_info(html)
    singer_indos = get_singer_info(html)
    for singer_info in singer_indos:
        lyric = get_lyric(singer_info[1])
        write_lyric(singer_info[0], lyric)
        download_song(singer_info[0], singer_info[1])
