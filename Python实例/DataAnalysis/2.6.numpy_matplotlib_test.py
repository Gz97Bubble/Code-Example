# coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
"""
希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改
点击, 喜欢, 不喜欢, 评论数量(["views", "likes", "dislikes", "comment_total"])
"""

us_path = './youtube_video_data/US_video_data_numbers.csv'
uk_path = './youtube_video_data/GB_video_data_numbers.csv'

t_uk = np.loadtxt(uk_path, delimiter=',', dtype=int)

# 截取喜欢数和评论数小于50万的
t_uk = t_uk[t_uk[:, 1] <= 500000]
t_uk = t_uk[t_uk[:, -1] <= 500000]

# 取评论的数据和喜欢数的数据
t_uk_comments = t_uk[:, -1]
t_uk_like = t_uk[:, 1]

plt.figure(figsize=(18, 9), dpi=80)
plt.scatter(t_uk_like, t_uk_comments)
plt.show()

