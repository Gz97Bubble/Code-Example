# coding:utf-8
from selenium import webdriver

url = 'https://qzone.qq.com/'
option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

driver = webdriver.Chrome(options=option)

driver.get(url)

# 窗口切换
# driver.switch_to.frame('login_frame')
el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to.frame(el_frame)

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1320832596')
driver.find_element_by_id('p').send_keys('g15398131686z')
driver.find_element_by_id('login_button').click()

