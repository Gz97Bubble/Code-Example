import requests

url = "http://www.baidu.com"
response = requests.get(url)

print(len(response.content.decode()))
print(response.content.decode())

# 构建请求头字典
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
# 发送带请求头的请求
response1 = requests.get(url, headers = headers)

print(len(response1.content.decode()))
print(response1.content.decode())
