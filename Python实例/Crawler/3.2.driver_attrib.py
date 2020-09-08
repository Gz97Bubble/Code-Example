# coding:utf-8
from selenium import webdriver
import time

url = 'http://www.baidu.com'
option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

# 创建一个浏览器对象
driver = webdriver.Chrome(options=option)

# 访问指定的url地址
driver.get(url)

# 显示源码
print(driver.page_source)
# 显示响应对应的url
print(driver.current_url)
print(driver.title)

# time.sleep(2)
# driver.get('http://www.douban.com')
#
# time.sleep(2)
# driver.back()
#
# time.sleep(2)
# driver.forward()
#
# time.sleep(2)
# driver.close()

# 保存网页快照，常用于验证是否运行或者验证码截图
driver.save_screenshot('baidu.png')

driver.quit()
