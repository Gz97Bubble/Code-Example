# coding:utf-8
from jsonpath import jsonpath

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': 'python'}}}}}}

print(data['key1']['key2']['key3']['key4']['key5']['key6'])

# jsonpath的结果为列表，获取数据需要索引
print(jsonpath(data, '$.key1.key2.key3.key4.key5.key6'))
print(jsonpath(data, '$..key6')[0])
