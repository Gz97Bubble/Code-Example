# coding:utf-8
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

"""
假设现在我们有一组从2006年到2016年1000部最流行的电影数据，我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？

对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？

对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1

"""

file_path = './IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

# print(df.info())
# print(df.head(1))

# 获取电影的平均评分
print(df['Rating'].mean())

# 获取导演的人数
# print(len(set(df['Director'].tolist())))
print(len(df['Director'].unique()))

# 获取演员的人数
temp_actors_list = df['Actors'].str.split(',').tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actors_list))
print(actors_num)


# # rating,runtime分布情况进行呈现
# # 选择图形,直方图
# # 准备数据
# runtime_data = df['Runtime (Minutes)'].values
#
# max_runtime = runtime_data.max()
# min_runtime = runtime_data.min()
# # 计算组数
# num_bin = (max_runtime - min_runtime)//5
# print(max_runtime - min_runtime)
#
# # 设置图像大小
# plt.figure(figsize=(18, 9), dpi=80)
# plt.hist(runtime_data, num_bin)
#
# plt.xticks(range(min_runtime, max_runtime+5)[::5])
#
# plt.show()


# 统计分类的列表
print(df['Genre'])
temp_list = df['Genre'].str.split(',').tolist()  # [[], [], []..]

genre_list = list(set(i for j in temp_list for i in j))

# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
print(zero_df)
# 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zero_df.loc[i, temp_list[i]] = 1

print(zero_df)
# 统计每个分类的电影的数量
genre_count = zero_df.sum(axis=0)
print(genre_count)
# 排序
genre_count = genre_count.sort_values()
print(genre_count)
# 画图
_x = genre_count.index
_y = genre_count.values
plt.figure(figsize=(18, 9), dpi=80)
plt.bar(_x, _y)
plt.xticks(range(len(_x)), _x)
plt.show()
