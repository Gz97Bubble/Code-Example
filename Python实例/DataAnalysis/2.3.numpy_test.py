# coding:utf-8
import numpy as np

""""
现在希望把之前案例中两个国家的数据方法一起来研究分析，同时保留国家的信息（每条数据的国家来源），应该怎么办
"""

us_data = './youtube_video_data/US_video_data_numbers.csv'
uk_data = './youtube_video_data/GB_video_data_numbers.csv'
# 加载国家数据
us_data = np.loadtxt(us_data, delimiter=',', dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=',', dtype=int)

# 填你家国家信息
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)  # 构造全为0的数据
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)  # 构造全为0的数据

# 分别添加一列全为0,1的数据
us_data = np.hstack((zeros_data, us_data))
uk_data = np.hstack((ones_data, uk_data))

# 拼接两者数据
final_data = np.vstack((us_data, uk_data))
print(final_data)

# # 创建一个对角线为1的方阵,其他为0
# print(np.eye(3))
# # 获取最大值与最小值的位置
# t = np.eye(4)
# print(np.argmax(t, axis=0))  # 第一维(行)上的最大值

# # 生成随机数
# # .rand(d0, d1, d2...dn)  # 均匀分布,范围0-1
# # .randn(d0, d1, d2...dn)  # 正态分布,浮点数,平均数0,标准差1
# # .randint(low, high, (shape))  # 从给定上下限范围选取随机数整数,范围是low,high,包含low但小于high,形状是shape
# t1 = np.random.randint(10, 20, (4, 5))  # 创建一个四行五列的数组,数值介于10和20之间
# print(t1)
# # .uniform(low, high, (size))  # 产生具有均匀分布的数组,low起始值,high结束值,size形状
# t1 = np.random.uniform(10, 20, (4, 5))  # 创建一个四行五列的数组,带有小数,数值介于10和20之间
# print(t1)

# np.random.seed(10)  # 随机种子,设定相同的种子,可以每次都生成相同的随机数
# t1 = np.random.randint(0, 20, (3, 4))
# print(t1)


# # copy和view
# a = b  # 完全不复制,ab相互影响
# a = b[:]  # 视图操作,一种切片,会创建新的a对象,但是a的数据完全由b保管,数据变化一致
# a = b.copy()  # 复制,a和b互不影响

