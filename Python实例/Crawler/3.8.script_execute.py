# coding:utf-8
from selenium import webdriver
import time

url = 'https://jn.lianjia.com/'

option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

driver = webdriver.Chrome(options=option)

driver.get(url)

# 滚动条的拖动

js = 'scrollTo(0, 1000)'
# 执行js
driver.execute_script(js)

time.sleep(2)

# el_button = driver.find_element_by_xpath('//*[@id="ershoufanglist"]/div/ul/li[1]/a/div/img')
el_button = driver.find_element_by_partial_link_text(u'更多济南二手房')

el_button.click()
