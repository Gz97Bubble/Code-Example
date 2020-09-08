# coding:utf-8
import js2py
import requests

# 创建js执行环境
context = js2py.EvalJs()
# 加载js文件
headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
}
big_js = requests.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js', headers=headers).content.decode()

context.execute(big_js)

# context.execute('setMaxDigits(130);')

context.t = {'class': 'python21'}

print(context.t)
print(type(context.t))
