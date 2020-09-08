# coding:utf-8
# from selenium import webdriver
#
# option = webdriver.ChromeOptions()
# option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'
#
# # 如果driver没有添加到了环境变量，则需要将driver的绝对路径赋值给executable_path参数
# # driver = webdriver.Chrome(executable_path='')
#
# # 如果driver添加了环境变量则不需要设置executable_path
# driver = webdriver.Chrome(options=option)
#
# # 向一个url发起请求
# driver.get('https://www.itcast.cn/')
#
# # 把网页保存为图片，69版本以上的谷歌浏览器将无法使用截图功能
# # driver.save_sreenshot('itcast.png')
#
# print(driver.title) # 打印页面的标题
#
# # 退出模拟浏览器
# driver.quit() # 一定要退出！不退出会有残留进程！


import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

# 通过指定chromedriver的路径来实例化driver对象，chromedriver放在当前目录。
# driver = webdriver.Chrome(executable_path='./chromedriver')
# chromedriver已经添加环境变量
desired_capabilities = option.to_capabilities()
driver = webdriver.Chrome(options=option)

# 控制浏览器访问url地址
driver.get("https://www.baidu.com/")
time.sleep(3)

# 在百度搜索框中搜索'python'
driver.find_element_by_id('kw').send_keys('python')
# 点击'百度搜索'
driver.find_element_by_id('su').click()

time.sleep(6)
# 退出浏览器
driver.quit()
