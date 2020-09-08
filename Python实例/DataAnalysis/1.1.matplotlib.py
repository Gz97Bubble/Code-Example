# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# figsize:设置宽和高，目前是宽18高9,dpi设置每英寸点的个数，目前是80个
plt.figure(figsize=(18, 9), dpi=80)

# plot:绘制直线图，可同时多绘制多个线 用处:反映同一事物在不同时间里的发展变化的情况
# color指定颜色，linestyle设置样式，linewidth设置粗细，alpha设置透明度，用label标识，添加图例legend显示各线条的label
# plt.plot(x, y, color='orange', linestyle='-.', label='第一条线')
# plt.legend()

# plt.scatter(x, y)  # 绘制散点图 用处:不同条件(维度)之间的内在关联关系/观察数据的离散聚合程度

# plt.bar(x, y, width=0.5)  # 绘制条形图 用处:数量统计/频数统计(市场饱和度)
# plt.barh(x, y, height=0.5)  # 绘制横着的条形图，与bar相比ticks和label的xy要进行反转

# plt.hist(a, num_bin, density=True)  # 绘制直方图 用处:显示分布状态
# a为需要统计的数据（列表形式，是没有统计过的数据，统计过的可用条形图），num_bin为组距，density设置百分比显示。

# matplotlib默认不支持中文字体，通过matplotlib.rc可以修改，或通过font_manager解决
plt.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rc("font", family='SimHei', weight='bold')

# 设置x轴和y轴的刻度,可通过xticks(a, b)使用字符串列表b做x轴，b要与a一一对应
# plt.xticks(x)
# plt.xticks(range(2, 25))
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::2])
plt.yticks(range(min(y), max(y)+1))

# 添加描述信息
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('实验')

# savefig:保存图片 可以保存为svg矢量图格式，放大不会有锯齿
# plt.savefig('./t1.png')
# plt.savefig('./t1.svg')

# grid绘制网格
# plt.grid(alpha=0.4, linestyle=':')  # alpha设置透明度,linestyle设置网格样式

# show:展示图形
plt.show()
