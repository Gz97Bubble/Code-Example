# coding:utf-8
import requests
import json
import sys


class King(object):

    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        self.data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }
        pass

    def get_data(self):
        # 使用post方法发送一个post请求，data为请求体的字典
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return response.content

    def parse_data(self, data):
        # loads方法将json字符串转化为python字典
        dict_data = json.loads(data)
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    def run(self):
        # 编写爬虫逻辑

        # url
        # headers
        # data字典
        # 发送请求获取响应
        response = self.get_data()
        print(response)

        # 数据解析
        self.parse_data(response)


if __name__ == '__main__':
    # word = input('请输入要翻译的单词或句子:')
    word = sys.argv[1]
    king = King(word)
    king.run()
