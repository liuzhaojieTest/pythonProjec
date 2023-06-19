import requests

try:
    response = requests.get('http://www.example.com/')
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print('HTTP error occurred: %s' % e)
except requests.exceptions.ConnectionError as e:
    print('Connection error occurred: %s' % e)
except requests.exceptions.Timeout as e:
    print('Timeout error occurred: %s' % e)
except requests.exceptions.RequestException as e:
    print('An error occurred: %s' % e)