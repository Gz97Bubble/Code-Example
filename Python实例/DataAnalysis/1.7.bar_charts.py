# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

""""
假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,为了展示列表中电影本身的票房以及同
其他电影的数据对比情况,应该如何更加直观的呈现该数据?
"""
a = {"猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"}
b_16 = {15746, 312, 4497, 319}
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(16, 8), dpi=80)
bar_distance = 0.2
x_14 = list(range(len(a)))
x_15 = [i+bar_distance for i in x_14]
x_16 = [i+bar_distance for i in x_15]
plt.bar(x_14, b_14, width=bar_distance, label='9月14日')
plt.bar(x_15, b_15, width=bar_distance, label='9月15日')
plt.bar(x_16, b_16, width=bar_distance, label='9月16日')
plt.legend(loc='upper left')

# 设置x刻度
plt.xticks(x_15, a)

# 设置说明
plt.title('电影票房')
plt.xlabel('电影')
plt.ylabel('票房')

plt.show()
