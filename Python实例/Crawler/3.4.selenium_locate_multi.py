# coding:utf-8
from selenium import webdriver
import time

url = r'https://fy.58.com/hezu/?PGTID=0d100000-0091-5a18-1f18-eff08ff68194&ClickID=2'
option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'
driver = webdriver.Chrome(options=option)

driver.get(url)

el_list = driver.find_elements_by_xpath('//ul[contains(@class,"house-list")]/li/div[2]/h2/a')

for el in el_list:
    print(el.text, el.get_attribute('href'))

    # el.click()
    # el.send_keys(data)  el必须是 text input标签
    # el.clear() # 对输入框作清空操作


time.sleep(2)
driver.quit()
