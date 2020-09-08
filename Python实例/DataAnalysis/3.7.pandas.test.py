# coding:utf-8
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
""""
现在我们有全球排名靠前的10000本书的数据，那么请统计一下下面几个问题：
1.不同年份书的数量
2.不同年份书的平均评分情况
"""

file_path = './books.csv'

df = pd.read_csv(file_path)

# print(df.head(1))
# print(df.info())

data_without_NaN = df[pd.notnull(df['original_publication_year'])]

# 不同年份书的数量
grouped = data_without_NaN.groupby(by='original_publication_year').count()['title']

# 不同年份书的平均评分情况
grouped = data_without_NaN['average_rating'].groupby(by=data_without_NaN['original_publication_year']).mean()
# print(grouped, type(grouped))

x = grouped.index
y = grouped.values

plt.figure(figsize=(18, 9), dpi=80)
plt.plot(range(len(x)), y)
plt.xticks(range(len(x))[::20], x[::20].astype(int), rotation=45)
plt.show()
