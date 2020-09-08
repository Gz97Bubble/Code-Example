# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

"""
在美国2004年人口普查发现有124 million的人在离家相对较远的地方工作。根据他们从家到上班地点所需要的时间,通过抽样统计
(最后一列)出了下表的数据,这些数据能够绘制成直方图么?
"""
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 设置图形大小
plt.figure(figsize=(18, 9), dpi=80)

plt.bar(range(12), quantity, width=1)

# 设置x轴的刻度
x_ = [i-0.5 for i in range(13)]
x_ticks = interval + [150]
plt.xticks(x_, x_ticks)


plt.grid(alpha=0.3, linestyle='--')
plt.show()
