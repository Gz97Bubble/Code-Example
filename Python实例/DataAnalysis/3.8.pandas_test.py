# coding:utf-8
import pandas as pd
import numpy as np
import xlrd
from matplotlib import pyplot as plt
import matplotlib

"""
现在我们有2015到2017年25万条911的紧急电话的数据，请统计出出这些数据中不同类型的紧急情况的次数，
统计出911数据中不同月份电话次数的变化情况
如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
"""

file_path = './911.xlsx'

df = pd.read_excel(file_path)


# print(df.info())
# print(df.head())

# # 获取分类情况
# # print(df['title'].str.split(':'))
# temp_list = df['title'].str.split(':').to_list()
# cate_list = list(set([i[0] for i in temp_list]))
# # print(cate_list)  # 得出三个分类
# 构造全为0的数组
# zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
#
# # 赋值
# # for cate in cate_list:
# #     zeros_df[cate][df['title'].str.contains(cate)] = 1
# #
# # print(zeros_df)
# for i in range(df.shape[0]):
#     zeros_df.loc[i, temp_list[i][0]] = 1
#
# sum_ret = zeros_df.sum(axis=0)
# print(sum_ret)

# temp_list = df['title'].str.split(':').to_list()
# cate_list = [i[0] for i in temp_list]
# cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)), columns=['cate'])
# # print(cate_df)
# df['cate'] = cate_df
# # print(df.head())  # 多出一列cate
# print(df.groupby(by='cate').count()['title'])


# #　统计出911数据中不同月份电话次数的变化情况
# df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# df.set_index('timeStamp', inplace=True)
# # print(df.head(5))
# count_by_month = df.resample('M').count()['title']
# # print(count_by_month)
#
# x = count_by_month.index
# y = count_by_month.values
# _x = [i.strftime('%Y-%m-%d') for i in x]
#
# plt.figure(figsize=(18, 9), dpi=80)
# plt.plot(range(len(x)), y)
# plt.xticks(range(len(x)), _x, rotation=45)
# plt.show()


# # 如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
# 把时间字符串转为时间类型,之后设置为索引
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# 添加列,表示分类
temp_list = df['title'].str.split(':').to_list()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
df.set_index('timeStamp', inplace=True)
# 分组
plt.figure(figsize=(18, 9), dpi=80)
for group_name, group_data in df.groupby(by='cate'):
    # 对不同的分类进行绘图
    count_by_month = group_data.resample('M').count()['title']
    x = count_by_month.index
    y = count_by_month.values
    _x = [i.strftime('%Y-%m-%d') for i in x]  # 转化时间格式,转为每年每月每日
    plt.plot(range(len(x)), y, label=group_name)

plt.legend()
plt.xticks(range(len(x)), _x, rotation=45)
plt.show()
