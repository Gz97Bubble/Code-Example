# coding:utf-8
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

"""
现在我们有北上广、深圳、和沈阳5个城市空气质量数据，请绘制出5个城市的PM2.5随时间的变化情况
观察这组数据中的时间结构，并不是字符串，这个时候我们应该怎么办？
"""

file_path = './PM2.5/BeijingPM20100101_20151231.csv'

df = pd.read_csv(file_path)
# print(df.head())
# print(df.info())

period = pd.PeriodIndex(year=df['year'], month=df['month'], day=df['day'], hour=df['hour'],
                        freq='H')
# print(period, type(period))
df['datetime'] = period

# 把datetime设置为索引
df.set_index('datetime', inplace=True)

# 进行降采样
df = df.resample('7D').mean()

# 处理缺失数据,删除缺失数据
# print(df['PM_US Post'])
data = df['PM_US Post'].dropna()
data_CN = df['PM_Dongsi'].dropna()

# 画图
x_US = data.index
y_US = data.values
x_CN = data_CN.index
y_CN = data_CN.values

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(x_US)), y_US, label='US_POST')
plt.plot(range(len(x_CN)), y_CN, label='CN_POST')
plt.legend(loc='best')
plt.xticks(range(0, len(x_US), 10), list(x_US)[::10], rotation=45)
plt.show()
