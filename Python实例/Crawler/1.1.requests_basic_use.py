import requests

url = "http://www.baidu.com"
response = requests.get(url)

# # 手动设定编码格式
# esponse.encoding = "utf8"
# # 打印源码的str类型数据
# print(response.text)
# print(response.encoding)

# # response.content是存储的bytes类型的响应源码，可以进行decode操作,默认UTF8
# print(response.content)
# print(response.content.decode())

# # 常见的相应对象参数和方法
# # 相应url
# print(response.url)

# # 状态码
# print(response.status_code)

# # 相应对应的请求头
# print(response.request.headers)
# # 相应头
# print(response.headers)

# # 答应响应设置cookies
# print(response.cookies)
