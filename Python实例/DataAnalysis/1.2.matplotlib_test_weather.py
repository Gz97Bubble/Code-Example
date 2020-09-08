# coding:utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

"""如果列表a表示10点到12点每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况？"""
a = [random.randint(20, 35) for i in range(120)]


y = a
x = range(0, 120)

plt.figure(figsize=(18, 9), dpi=80)

plt.plot(x, y)

# 设置中文显示，windows和linux设置字体的方式
# my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simfang.ttf')
plt.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rc("font", family='SimHei', weight='bold', size='larger')

# 调整x轴的刻度,使用字符串做x轴的刻度
x_ticks = ['10点{}分'.format(i) for i in x[:60]] + ['11点{}分'.format(i) for i in x[:60]]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(x[::10], x_ticks[::10], rotation=45)  # rotation旋转的度数，逆时针旋转

# 添加描述信息
plt.xlabel('时间')
plt.ylabel('温度 单位(℃)')
plt.title('10点到12点每分钟的气温变化情况')

plt.show()
