# coding:utf-8
import numpy as np

"""
读取数据:np.loadtxt(frame.dtype=np.float, delimiter=None, skiprows=0, usecols=None, unpack=False)
dtype数据类型,默认np.float; delimiter:分隔字符串,默认是空格,可改为逗号; skiprows:跳过前x行,默认跳过第一行表头
usecols:读取指定的列,索引元祖类型; unpack:如果True,读入属性将写入不同的数组变量,默认False只写入一个,相当于转置
"""

"""
现在这里有一个英国和美国各自youtube1000多个视频的点击, 喜欢, 不喜欢, 评论数量(["views", "likes", "dislikes", "comment_total"])
的csv, 运用刚刚所学习的只是, 我们尝试来对其进行操作
数据来源: https://www.kaggle.com/datasnaek/youtube/data
"""
us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

f1 = np.loadtxt(us_file_path, delimiter=',', dtype=int)  # delimiter，dtype常用
# f1 = np.loadtxt(us_file_path, delimiter=',', dtype=int, unpack=True)  # 转置:行变列,列变行
# # 转置可用:
# f1.transpose() / f1.T / f1.swapaxes(1, 0)
print(f1)

print('*' * 100)
# # 取行
# print(f1[2])  # 取第二行
# # 取连续的多行
# print(f1[2:])   # 取第二行到最后一行
# # 取不连续的多行
# print(f1[[1, 2, 3]])  # 取第二第三第四行

# # 取列
# print(f1[:, 1])  # 取第二列
# # 取连续的多列
# print(f1[:, 2:])  # 取第三列和第四列
# # 取不连续的多列
# print(f1[:, [0, 2]])  # 取第一列和第三列

# # 取行和列
# print(f1[1, 2])  # 取第二行第三列的值
# print(f1[1:2, 2:3])  # 也是取第二行第三列的值，但输出是列表
# print(f1[1:3, 2:4])  # 取第二行到第三行的第三列到第四的值

# # 取多个不相邻的点
# print(f1[[0, 2, 2], [0, 1, 3]])  # 在列表中得到[0, 0]和[2, 1],[2, 3]的点

# # 数值的修改
# t1 = np.arange(24).reshape(4, 6)
# print(t1)
# print(t1 < 10)  # 列表内输出bool类型
# t1[t1 < 10] = 3  # 小于10的赋值为3
# print(t1)
#
# t1 = np.where(t1 <= 3, 100, 300)  # 小于等于的赋值为3,其他的赋值为300
# print(t1)
#
# t1 = t1.clip(200, 250)  # 小于200的替换为200,大于250的替换为250
# print(t1)
#
# t1 = t1.astype('float')  # nan是浮点类型的
# t1[2, 2] = np.nan  # 将第三行第三列赋值为nan
# print(t1)

# # 数值的拼接
# t1 = np.arange(12).reshape(2, 6)
# t2 = np.arange(12, 24).reshape(2, 6)
# print(t1)
# print(t2)
# print(np.vstack((t1, t2)))  # 竖直拼接(vertically)
# print(np.hstack((t1, t2)))  # 水平拼接(horizontally)

# # 行与列进行交换
# t1 = np.arange(12).reshape(3, 4)
# print(t1)
# t1[[1, 2], :] = t1[[2, 1], :]  # 第二行与第三行进行交换
# print(t1)
# t1 = np.arange(12).reshape(3, 4)
# t1[:, [0, 2]] = t1[:, [2, 0]]  # 第一列与第三列进行交换
# print(t1)
