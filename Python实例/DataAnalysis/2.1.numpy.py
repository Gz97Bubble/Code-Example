# coding:utf-8
import numpy as np
import random

# 使用numpy生成数组，得到ndarray的类型
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(4, 10, 2)
print(t3)
print(t3.dtype)

print('*' * 100)
# numpy中的数据类型
t4 = np.array(range(1, 4), dtype='float')
print(t4)
print(t4.dtype)

# numpy中的布尔类型
t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)
print(t5)
print(t5.dtype)

print('*' * 100)
# 调整数据类型:astype()方法
t6 = t5.astype('int8')
print(t6)
print(t6.dtype)

print('*' * 100)
# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

# 取小数
t8 = np.round(t7, 2)  # 保留两位小数
print(t8)

print('*' * 100)
# 数据的形状
print(t1.shape)  # 2行
t9 = np.array([[1, 2, 3], [2, 3, 4]])
print(t9.shape)  # 2行3列
print(t9.shape[0])  # 输出2

print('*' * 100)
# 更改数组形状
t10 = np.arange(12)
print(t10)
print(t10.reshape((3, 4)))
t11 = np.arange(24).reshape((2, 3, 4))
print(t11)
print(t11.reshape(4, 6))
t12 = t11.reshape(24, )  # 变回一维数组
t12 = t11.reshape((t11.shape[0] * t11.shape[1] * t11.shape[2],))  # 变回一维数组
t12 = t11.flatten()  # 变回一维数组
print(t12)

print('*' * 100)
# 数组加减乘除
print(t12 + 2)
print(t12 * 2)
# print(t12 / 0)  # 可执行 nan表示0/0, inf表示无限

print('*' * 100)
# 数组之间的计算
t12 = t12 + t12  # 对应值相加
print(t12)
t13 = np.array(t10.reshape((3, 4)) - list(range(4)))  # 前者(3,4)没一行都减去后者(,4)
print(t13)
# 同理，shape为(3,3,2)与(3,2)的数组也可以进行计算

print('*' * 100)

# # NAN和inf:nan与inf都是float类型的
print(np.nan == np.nan)  # 两个nan是不相等的，
print(np.nan != np.nan)  # 两个nan是不相等的，
t14 = np.arange(24).reshape(4, 6).astype(float)
t14[3, 4] = np.nan
print(t14)
print(np.isnan(t14))  # 判断是否是nan
print(np.sum(t14))  # nan与任何数计算都是nan
print(np.sum(t14, axis=0))  # 每一列的数组相加,nan与任何数计算都是nan
# print(np.sum(t14, axis=1))  # 每一行的数组相加,nan与任何数计算都是nan
print(t14.mean(axis=0))  # 每一列的数组的均值
# print(t14.mean(axis=1))  # 每一行的数组的均值
print(np.median(t14, axis=0))  # 每一列的数组的均值
# print(np.median(t14, axis=1))  # 每一行的数组的均值
print(np.max(t14, axis=0))  # 每一列的数组的最大值
print(np.max(t14, axis=1))  # 每一行的数组的最大值
# print(np.min(t14, axis=0))  # 每一列的数组的最小值
