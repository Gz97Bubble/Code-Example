# coding:utf-8
from selenium import webdriver

url = 'http://www.baidu.com'

option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

driver = webdriver.Chrome(options=option)
# 设置位置之后的所有元素定位操作都有最大等待时间十秒，在10秒内会定期进行元素定位，超出定位时间之后将会报错
driver.implicitly_wait(10)

driver.get(url)

el = driver.find_element_by_xpath('//*[@id="s_lg_img"]')
print(el)
