# coding:utf-8
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
""""
使用matplotlib呈现出店铺总数排名前10的国家
使用matplotlib呈现出每个中国每个城市的店铺数量
"""
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
file_path = './starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)

# # 使用matplotlib呈现出店铺总数排名前10的国家
# # 准备数据
# data_country_count = df.groupby(by='Country').count()['Brand'].sort_values(ascending=False)[:10]
#
# x = data_country_count.index
# y = data_country_count.values
#
# plt.figure(figsize=(18, 9), dpi=80)
# plt.bar(range(len(x)), y)
# plt.xticks(range(len(x)), x)
# plt.show()

df = df[df['Country'] == 'CN']
print(df.head(1))

data_country_count = df.groupby(by='City').count()['Brand'].sort_values(ascending=False)[:25]

x = data_country_count.index
y = data_country_count.values

plt.figure(figsize=(18, 9), dpi=80)
plt.bar(range(len(x)), y, width=0.5, color='orange')
plt.xticks(range(len(x)), x, rotation=45)
plt.show()
