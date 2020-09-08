# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

""""
假设大家在30岁的时候，根据自己的实际情况，统计出来了从11岁到30岁每年交的男女朋友的数量如列表a，请绘制出该数据的折线图，以便分析自己每年交男女朋友的数量走势。
要求:
    y轴表示个数
    x轴表示岁数，比如11岁，12岁
"""
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]


y = a
x = [i for i in range(11, 31)]

plt.figure(figsize=(10, 5), dpi=80)

plt.plot(x, y)

plt.rcParams['font.sans-serif'] = ['SimHei']

x_label = ['{0}岁'.format(i) for i in x]
plt.xticks(x)
plt.yticks(range(min(y), max(y)+1))

plt.title('11岁到30岁每年交的男女朋友的数量')
plt.xlabel('年龄')
plt.ylabel('人数')

plt.grid(alpha=0.2)

plt.show()
