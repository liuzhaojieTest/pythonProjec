from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyppeteer
from bs4 import BeautifulSoup

# driver = webdriver.Edge()
# driver.minimize_window()
# driver.get('https://nnyy.best/movie/312719/')
# html = driver.page_source
# # response = requests.get('https://nnyy.best/movie/312719/',
# #                         headers={'User-Agent': 'Mozilla/5.0'}, data=html.encode('utf-8'))
#
# # driver.quit()
#
# # from bs4 import BeautifulSoup
# # import lib
# # url = 'https://nnyy.best/movie/312719/'
# # response = requests.get(url)
# soup = BeautifulSoup(html, 'html.parser')
# video = soup.find('video')
# # print(type(video))
# src = video['src']
# print(src)
# response = urlcleanup('blob:https://www.iqiyi.com/0c6a93bd-3208-4629-bef4-2be4f9e61e59')
# print(response)
# src = 'https://nnyy.best/movie/312719/'
# with open('D:/Test/MP3/video.mp4', 'wb')as f:
#     f.write()
from pydub import AudioSegment

input_file = "D:/Test/MP3/时光洪流.mp3"
output_file = "D:/Test/MP3/时光洪流.wav"
sound = AudioSegment.from_file(input_file, format="mp3")
sound.export(output_file, format="wav")
