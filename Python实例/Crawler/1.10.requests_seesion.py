# coding:utf-8
import requests
import re

def login():
    # session
    session = requests.session()

    # headers
    session.headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.100Safari / 537.36'
    }

    # url1-获取token
    url1 = 'https://github.com/login'
        # 发送请求获取响应
    res_1 = session.get(url1).content.decode()
        # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]

    # url2-登录
    url2 = 'https://github.com/session'
        # 构建表单数据
    data = {
        'commit': 'Sign in',
        'authenticity_token': token,
        'login': '1320832596 @ qq.com',
        'password': 'g15398131686z',
        'webauthn - support': 'supportedwebauthn - iuvpaa - support: unsupported',
        'return_to': '',
        'required_field_d859': '',
        'timestamp': '1597495618719',
        'timestamp_secret': '3f893db2943b1a24cace10101241ff03b6761fd408682691127c225199f859fa'
    }
    # print(data)
        #发送请求登录
    session.post(url2, data=data)

    # url3-验证
    url3 = 'https://github.com/g1320832596z'
    response = session.get(url3)
    with open('github.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    login()