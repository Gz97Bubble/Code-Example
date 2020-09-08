# coding:utf-8
import pandas as pd
import numpy as np

"""
现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？
"""

file_path = './starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
# grouped = df.groupby(by='Country')
# print(grouped)  # DataFrameGroupBy可以进行遍历、调用聚合方法
# 遍历
# for i, j in grouped:
#     print(i)
#     print('-' * 100)
#     print(j)
#     print('*' * 100)
# 调用聚合方法
# country_count = grouped['Brand'].count()
# print(country_count)
# print(country_count['US'])
# print(country_count['CN'])


# 统计中国每个省份的店铺的数量
china_data = df[df['Country'] == 'CN']
grouped = china_data.groupby(by='State/Province').count()['Brand']
print(grouped)

# 数据按照多个条件进行分组
grouped = df['Brand'].groupby(by=[df['Country'], df['State/Province']]).count()
print(grouped)
print(type(grouped))  # Series类型

# 数据按多个条件进行分组,返回DataFrame
grouped = df[['Brand']].groupby(by=[df['Country'], df['State/Province']]).count()  # columns取双列
# grouped = df.groupby(by=[df['Country'], df['State/Province']]).count()[['Brand']]
# grouped = df.groupby(by=[df['Country'], df['State/Province']])[['Brand']].count()
print(grouped, type(grouped))  # DataFrame类型

# 索引的方法和属性
print(grouped.index)
