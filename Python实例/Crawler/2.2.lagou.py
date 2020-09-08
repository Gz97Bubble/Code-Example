# coding:utf-8
import requests
import jsonpath
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

response = requests.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json', headers=headers)

dict_data = json.loads(response.content)

print(jsonpath.jsonpath(dict_data,'$..A..name'))
