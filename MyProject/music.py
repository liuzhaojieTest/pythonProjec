# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import urllib
# import os
# from selenium import webdriver
# from time import sleep
#
#
# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0(Windows NT 6.1; WOW64)',
#         'Referer': 'http://music.163.com',
#         'Host': 'music.163.com'
#     }
#
#     try:
#         response = requests.get(url, headers=headers)
#         html = response.text
#         return html
#     except:
#         print('request error')
#         pass
#
#
# def get_singer_info(html):
#     soup = BeautifulSoup(html, 'lxml')
#     links = soup.find('ul', class_='f-hide').find_all('a')
#     song_IDs = []
#     song_names = []
#     # print(links)
#     for link in links:
#         song_ID = link.get('href').split('=')[-1]
#         song_name = link.get_text()
#         print(song_name)
#         print(song_ID)
#         song_IDs.append(song_ID)
#         song_names.append(song_name)
#     return zip(song_names, song_IDs)
#
#
# def get_lyric(song_id):
#     url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
#     html = get_html(url)
#     json_obj = json.loads(html)
#     initial_lyric = json_obj['lrc']['lyric']
#     # print(lyric)
#     regex = re.compile(r'\[.*\]')
#     final_lyric = re.sub(regex, '', initial_lyric).strip()
#     return final_lyric
#
#
# def write_lyric(song_name, lyric):
#     print('正在写入歌曲：{}'.format(song_name))
#     with open('D:/Test/TXT/{}.txt'.format(song_name), 'a', encoding='utf-8') as fp:
#         fp.write(lyric)
#
#
# def download_song(song_name, song_id):
#     sinnger_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
#     print('正在下载歌曲：{}'.format(song_name))
#     urllib.request.urlretrieve(sinnger_url, f'E:/MP3/{song_name}.mp3')
#
#
# def downLoad(song_name, song_id):
#     sinnger_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
#     print('正在下载歌曲：{}'.format(song_name))
#     res = requests.request(method="get", url=sinnger_url)
#     with open(f'D:/Test/MP3/{song_name}.mp3', "wb") as f:
#         f.write(res.content)
#
#     # print(html)
#     # with open('test.html', 'w', encoding='utf-8') as f:
#     #     f.write(html)
#     # with open('test.txt', 'r', encoding='utf-8') as f:
#     #     html = f.read()
#     # print(html)
#     # path = r'E:\PycharmProject\MyProject\venv\Scripts\chromedriver.exe'
#     # drive = webdriver.Chrome(executable_path=path)
#     # drive.get('http://www.baidu.com')
#     # sleep(5)
import requests
from bs4 import BeautifulSoup

# 请求头信息
headers = {
    'Referer': 'https://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'
}


# 获取歌曲列表
def get_song_list(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    song_list = soup.select('ul.f-hide li a')
    return song_list


# 获取歌曲详情
def get_song_detail(song_id):
    url = 'https://music.163.com/api/song/detail/?id={}&ids=[{}]'.format(song_id, song_id)
    res = requests.get(url, headers=headers)
    song_detail = res.json()['songs'][0]
    return song_detail


# 获取歌曲下载链接
def get_song_url(song_id):
    url = 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    return url


# 示例用法
if __name__ == '__main__':
    # 网易云音乐热歌榜URL
    url = 'https://music.163.com/discover/toplist?id=3778678'
    # url = 'http://music.163.com/artist?id=6731'
    song_list = get_song_list(url)
    # print(song_list)
    for song in song_list:
        song_id = song['href'].split('=')[-1]
        # print(song_id)
        song_detail = get_song_detail(song_id)
        # print(song_detail)
        song_url = get_song_url(song_id)
        print('歌名：{}，歌手：{}，专辑：{}，下载链接：{}'.format(song_detail['name'], song_detail['artists'][0]['name'],
                                                           song_detail['album']['name'], song_url))
