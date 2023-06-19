from selenium import webdriver
from time import sleep
import pandas as pd

driver = webdriver.Edge()
driver.get('http://music.163.com')
driver.maximize_window()
sleep(5)

if __name__ == '__main__':
    word = input('')
