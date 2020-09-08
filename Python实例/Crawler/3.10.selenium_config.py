# coding:utf-8
from selenium import webdriver

url = 'http://www.baidu.com'

# 创建配置对象
option = webdriver.ChromeOptions()
# 添加配置参数
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'
# 设置浏览器为无头模式
option.add_argument('--headless')
option.add_argument('--disable-gpu')
# 更换ip代理必须重新启动浏览器
# option.add_argument('--proxy-server=http://60.2.145.75:3128')
# 更换user-agent
# option.add_argument('--user-agent=Mozilla/5.0 python37')


# 创建浏览器对象的时候添加配置对象
driver = webdriver.Chrome(options=option)

driver.get(url)

driver.save_screenshot('baidu_到此一游.png')
