# coding:utf-8
import requests

url = 'http://www.baidu.com'

# response = requests.get(url)
proxies = {
    'http': 'http://58.220.95.31:10174',
    # 'https': 'https://125.108.118.21:9000'
}

response = requests.get(url, proxies=proxies)

print(response.text)
