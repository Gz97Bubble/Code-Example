# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

""""
假设大家在30岁的时候，根据自己的实际情况，统计出来你和你同桌各自从11岁到30岁每年交的男女朋友的数量如列表a和b，请在一个图中绘制出该数据的折线图，
以便比较自己和同桌20年间的差异，同时分析每年交男女朋友的数量走势
要求:
    y轴表示个数
    x轴表示岁数
"""
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

y1 = a
y2 = b
x = [i for i in range(11,31)]

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(12, 6), dpi=80)

plt.plot(x, y1, label='自己', color='orange', linestyle='--')
plt.plot(x, y2, label='同桌', color='cyan', linestyle='-.')
plt.legend(loc='upper left')

x_ticks = ['{0}岁'.format(i) for i in x]
plt.xticks(x, x_ticks,rotation=45)
plt.yticks(range(min(a+b), max(a+b)+1))

plt.title('你和你同桌各自从11岁到30岁每年交的男女朋友的数量')
plt.xlabel('年龄')
plt.ylabel('人数')

plt.grid(alpha=0.4, linestyle=':')

plt.show()
