import requests
import re
from bs4 import BeautifulSoup
import json


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
        'Referer': 'http://music.163.com',
        'Host': 'music.163.com'
    }

    try:
        response = requests.get(url, headers=headers)
        html = response.text
        print(html)
        return html
    except:
        print('request error')
        pass


def get_singer_info(htmls):
    soup = BeautifulSoup(htmls, 'lxml')
    links = soup.find('ul', class_='f-hide').find_all('a')
    song_IDs = []
    song_names = []
    for link in links:
        song_ID = link.get('href').split('=')[-1]
        song_name = link.get_text()
        print(song_name)
        print(song_ID)
        song_IDs.append(song_ID)
        song_names.append(song_name)
        return zip(song_names, song_IDs)


def get_lyric(song_id):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    html = get_html(url)
    json_obj = json.loads(html)
    initial_lyric = json_obj['lrd']['lyric']
    # print(lyric)
    regex = re.compile(r'\[.*]')
    final_lyric = re.sub(regex, '', initial_lyric).strip()
    # print(final_lyric)
    return final_lyric


def write_text(song_name, lyric):
    print(f'正在写入歌曲：{song_name}')
    with open(f'{song_name}.txt', 'a', encoding='utf-8') as fp:
        fp.write(lyric)


def download(song_name, song_id):
    print(f'正在下载歌曲：{song_name}')
    url = f'http://music.163,com/artist?id={sing_id}'
    with open(f'D:/Test/{song_name}.mp3', 'a', encoding='utf-8') as f:
        f.write(url)


# url = 'https://music.163.com/'
# date = requests.get(url)
# # print(date.text)
# file = open('1.doc', 'w', encoding='utf-8')
# file.write(date.text)
if __name__ == '__main__':
    sing_id = input('请输入歌手ID：')
    start_url = f'http://music.163,com/artist?id={sing_id}'
    html = get_html(start_url)
    singer_infos = get_singer_info(html)
    for singer_info in singer_infos:
        lyric = get_lyric(singer_info[1])
        write_text(singer_info[0], lyric)
        download(singer_info[0],singer_info[1])
