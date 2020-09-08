# coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
""""
英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
点击, 喜欢, 不喜欢, 评论数量(["views", "likes", "dislikes", "comment_total"])
"""
us_path = './youtube_video_data/US_video_data_numbers.csv'
uk_path = './youtube_video_data/GB_video_data_numbers.csv'

t_us = np.loadtxt(us_path, delimiter=',', dtype=int)

# 取评论的数据
t_us_comments = t_us[:, -1]

# 选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments < 5000]

d = 50
bin_num = (t_us_comments.max() - t_us_comments.min())//d

# 绘图
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(18, 9), dpi=80)
plt.hist(t_us_comments, bin_num)

# 绘图细节

plt.show()
