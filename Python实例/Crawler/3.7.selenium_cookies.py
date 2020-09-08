# coding:utf-8
from selenium import webdriver

url ='http://www.baidu.com'
option = webdriver.ChromeOptions()
option.binary_location = r'E:\360\360cse\360Chrome\Chrome\Application\360chrome.exe'

driver = webdriver.Chrome(options=option)

driver.get(url)

print(driver.get_cookies())

# cookies = {}
# for data in driver.get_cookies():
#     cookies[data['name']] = data['value']

cookies = {data['name']: data['value']for data in driver.get_cookies()}

print(cookies)
