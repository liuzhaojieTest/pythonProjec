from Python练习100题.music import get_html, get_singer_info, get_lyric, write_lyric, downLoad

if __name__ == '__main__':
    singer_id = input('请输入歌手ID：')
    start_url = 'http://music.163.com/artist?id={}'.format(singer_id)
    html = get_html(start_url)
    get_singer_info(html)
    singer_indos = get_singer_info(html)
    for singer_info in singer_indos:
        lyric = get_lyric(singer_info[1])
        write_lyric(singer_info[0], lyric)
        # download_song(singer_info[0], singer_info[1])
        downLoad(singer_info[0], singer_info[1])
