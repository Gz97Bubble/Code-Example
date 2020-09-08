# coding:utf8
import requests

# url = "http://www.baidu.com/s?wd=python"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
#         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
# }
#
# response = requests.get(url, headers=headers)
#
# with open('baidu.html', 'wb') as f:
#     f.write(response.content)

url = "http://www.baidu.com/s?"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
# 构建参数字典
data = {
    'wd': 'python'
}
response = requests.get(url, headers=headers, params=data)

print(response.url)
with open('baidu1.html', 'wb') as f:
    f.write(response.content)
