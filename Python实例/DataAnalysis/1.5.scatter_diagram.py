# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

""""
假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),那么此时如何寻找出气温和随时间(天)变化的某种规律?
"""
a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
     22, 23]
b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
     12, 13, 6]

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 设置数据的x和y
y_3 = a
y_10 = b
x_3 = range(1, 32)
x_10 = range(51, 82)
# 设置图像大小
plt.figure(figsize=(18, 9), dpi=80)
# 绘制散点图与添加图例
plt.scatter(x_3, y_3, label='三月份')
plt.scatter(x_10, y_10, label='十月份')
plt.legend(loc='upper left')
# 设置xy轴的刻度
x_ = list(x_3)+list(x_10)
x_ticks = ['3月{}日'.format(i) for i in x_3] + ['10月{}日'.format(i) for i in x_10]
plt.xticks(x_[::3], x_ticks[::3], rotation=45)
plt.yticks(range(min(a+b), max(a+b)+1))
# 添加描述信息
plt.title('北京2016年3,10月份每天白天的最高气温')
plt.xlabel('时间')
plt.ylabel('温度℃')
# 显示图像
plt.show()
