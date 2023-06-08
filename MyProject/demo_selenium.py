from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
sleep(2)
driver.get('http://124.220.218.30:18080//dmsweb/index.html#')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="pane-account"]/form/div/div/div/div/input').send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="pane-account"]/form/div[2]/div/div/div/input').send_keys('123')
driver.find_element(By.XPATH, '//*[@id="pane-account"]/form/div[3]/div/button').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="app"]/section/div/aside/div/div[1]/div/ul/li[3]/span').click()
sleep(1)
driver.close()
snapshot(msg="请填写测试点.")
