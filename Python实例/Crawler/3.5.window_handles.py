# coding:utf-8
from selenium import webdriver
import time

url = r'https://jn.58.com'

option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

driver = webdriver.Chrome(options=option)

driver.get(url)
# 点击租房按钮
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

print(driver.page_source)
print(driver.current_url)

# 切换标签
driver.switch_to.window(driver.window_handles[-1])

el_list = driver.find_elements_by_xpath('//ul[contains(@class,"house-list")]/li/div[2]/h2/a')
print(len(el_list))

time.sleep(2)
driver.quit()
