# coding:utf-8
from selenium import webdriver
import time

url = r'http://www.baidu.com'
option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

driver = webdriver.Chrome(options=option)
driver.get(url)

# 通过Xpath进行元素定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python3')
# 通过css选择器进行元素定位
# driver.find_element_by_css_selector('#kw').send_keys('python3')
# 通过name属性值进行元素定位
# driver.find_element_by_name('wd').send_keys('python3')
# 通过class属性值进行元素定位
# driver.find_element_by_class_name('s_ipt').send_keys('python3')

# driver.find_element_by_id('su').click()

# 通过链接文本进行元素定位
# driver.find_element_by_link_text(u'贴吧').click()
# driver.find_element_by_partial_link_text(u'贴').click()

# 目标元素在当前html中是唯一标签的时候或者是众多定位出来的标签中的第一个的时候才能使用
# print(driver.find_element_by_tag_name('title'))

# find_element_by_xxx
#     定位到则是一个对象
#     定位不到则报错
# find_element_by_xxx
#     定位到则是一个含有元素的列表
#     定位不到是一个空列表


time.sleep(2)
driver.quit()
