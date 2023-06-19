import requests
a = requests.get('http://www.baidu.com')
print(a.status_code)
print(a.text)
print(a.headers)
