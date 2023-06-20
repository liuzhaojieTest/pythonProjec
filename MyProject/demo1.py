import requests
import json
import bs4

url = 'https://music.163.com/discover/toplist?id=3778678'
jieg = requests.get(url=url)
print(jieg.json())
