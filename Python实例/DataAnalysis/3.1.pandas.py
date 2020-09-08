# coding:utf-8
import numpy as np
import pandas as pd
import string

print('*' * 100 + 'Series 一维')
t = pd.Series([1, 2, 31, 12, 3, 4])  # 直接创建Series
print(t)  # 一维,带标签数组
print(type(t))

t2 = pd.Series([1, 23, 2, 2, 1], index=list('abcde'))  # 直接创建Series,指定索引
print(t2)

temp_dict = {
    'name': 'xiaohong',
    'age': 30,
    'tel': 10086}
t3 = pd.Series(temp_dict)  # 通过字典创建Series
print(t3)

a = {string.ascii_uppercase[i]: i for i in range(10)}
t4 = pd.Series(a)
print(t4)
t4 = pd.Series(a, index=list(string.ascii_uppercase[3: 13]))
print(t4)

print('*' * 100 + 'Series切片与索引')
# # Series切片与索引
print(t3)
print(t3['name'])  # 通过索引取值
print(t3[['name', 'age']])  # 通过索引取多值
print(t3[0])  # 通过顺序取值
print(t3[0:2])  # 通过顺序取连续多值

print('*' * 100)
print(t3.index)
print(type(t3.index))
for i in t3.index:  # index可迭代
    print(i)
print(list(t3.index))  # 可转换为列表
print(list(t3.index[:2]))

print('*' * 100)
print(t3.values)
print(type(t3.values))

print('*' * 100 + 'DataFrame 二维，Series容器')
# # DataFrame 二维，Series容器
d1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(d1)  # 额外存在的竖着一列是index,行索引,表明不同行,纵向索引0轴axis=0,横着一列为columns,列索引,表明不同列,纵向索引1轴axis=1
d1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('wxyz'))
print(d1)

temp_dict = {
    'name': ['xiaohong', 'xiaogang'],
    'age': [30, 20],
    'tel': [10086, 10010]
}
d2 = pd.DataFrame(temp_dict)  # 通过字典创建DataFrame
print(d2)
temp_dict = [
    {'name': 'xiaohong', 'age': 32, 'tel': 10010},
    {'name': 'xiaogang', 'tel': 10086},
    {'name': 'xiaowang', 'age': 22, 'tel': 10000}
]
d2 = pd.DataFrame(temp_dict)  # 通过字典创建DataFrame,空值为NaN
print(d2)
print(d2.index)
print(d2.columns)
print(d2.shape)  # 3行3列
print(d2.ndim)  # 显示维度
print(d2.head(2))  # 显示头几行,默认显示前5行
print(d2.tail(2))  # 显示后几行,默认显示前5行

print('*' * 100)
print(d2.info())  # 相关信息展示
print('*' * 100)
print(d2.describe())  # 统计数字情况,个数 平均值 标准差 最小值 三种中位数 最大值

# DataFrame中的排序方法
d2 = d2.sort_values(by='tel', ascending=False)

print('*' * 100 + 'DataFrame中的取行和列,结果依旧是DataFrame类型或Series类型(单行单列)')
# - 方括号写数组表示取行,对行进行操作
# - 方括号写字符串表示取列索引,对列进行操作
print(d2[::2])  # 输出前两行
print(d2[::2]['age'])  # 输出前两行的age列
print(d2['age'])  # 输出所有行的age列
print(type(d2['age']))

print('*' * 100 + 'DataFrame使用loc通过标签获取位置,结果可以是内部数据类型')
# 使用loc进行精确选择
d3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('wxyz'))
print(d3)
print('*' * 100)
print(d3.loc['a', 'z'])  # 取a行z列的值
print(d3.loc[['a', 'c'], ['w', 'y']])  # 取多行多列

print('*' * 100 + 'DataFrame使用iloc通过位置获取位置,结果可以是内部数据类型')
# 使用iloc进行精确选择
print(d3.iloc[1, 2])  # 取第二行第三列
print(d3.iloc[:, [2, 1]])

print('*' * 100 + 'DataFrame条件选择与赋值')
# DataFrame条件选择与赋值
print(d3[d3['z'] > 3])
print(d3[(d3['z'] > 3) & (d3['y'] > 8)])
d3.iloc[1:3, :2] = np.nan
print(d3)

print('*' * 100 + 'DataFrame缺失数据的处理')
# DataFrame缺失数据的处理 - Nan
print(pd.isnull(d3))  # pd.isnull判断是否为nan
print(pd.notnull(d3))  # pd.notnull判断是否不为nan
print(d3[pd.notnull(d3['w'])])  # 选择w列下不为nan的行
print(d3.dropna(axis=0))  # 删除有nan的行
# print(d3.dropna(axis=0, how='all'))  # 删除有行中全为nan的行
# print(d3.dropna(axis=0, how='all', inplace=False))  # 删除有行中全为nan的行,inplace是True的话是立刻修改内部值
print('*' * 100)
print(d3)
print(d3.fillna(100))  # 直接全部填充为100
print(d3.fillna(d3.mean()))  # 填充该列的均值
print(d3['w'].fillna(d3['w'].mean()))  # 只填充age一列的均值,可直接通过d3['age'] = d3['age']..代替

print('*' * 100)
# DataFrame缺失数据的处理 - 0
print(d3)
d4 = d3.copy()
d4[d4 == 0] = 1
print(d4)

print('*' * 100 + '数据合并 - join merge')
# # 数据合并 - join
j1 = pd.DataFrame(np.ones((2, 4)), index=['A', 'B'], columns=list('abcd'))
j2 = pd.DataFrame(np.zeros((3, 3)), index=['A', 'B', 'C'], columns=list('xyz'))
print(j1)
print(j2)
print(j1.join(j2))  # 默认情况下他是把行索引index相同的数据合并到一起,j1为主
print(j2.join(j1))  # 默认情况下他是把行索引index相同的数据合并到一起,j2为主

print('*' * 100)
j3 = pd.DataFrame(np.zeros((3, 3)), columns=list('fax'))
print(j3)
print(j1.merge(j3, on='a'))  # 按照指定的列把数据按照一定的方式合并到一起,on指定判断字段,该字段相同的行合并,不相同的行舍去
j3.loc[1, 'a'] = 1
print(j1.merge(j3, on='a', how='inner'))  # 默认inner,取交集
print(j1.merge(j3, on='a', how='outer'))  # 并集
print(j1.merge(j3, on='a', how='left'))  # 左边为准,NaN补全
print(j1.merge(j3, on='a', how='right'))  # 右边为准,Nan补全
print(j1.merge(j3, left_on='a', right_on='x'))  # 左边on为a,右边on为x

j1.loc[['A'], ['a']] = 100
print('*' * 100 + '索引和复合索引')
print(j1)
j1.index = ['a', 'b']
print(j1)
print(j1.reindex(['a', 'f']))

print('*' * 100)
print(j1.set_index('a'))  # 把当前DataFrame的某一列作为索引
print(j1['d'].unique())  # 取唯一值,输出array
print(j1['a'].unique())
print(j1.set_index('a').index.unique)  # index也可以输出唯一值

print('*' * 100)
a = pd.DataFrame({'a': range(7),
                  'b': range(7, 0, -1),
                  'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                  'd': list('hjklmno')
                  })
print(a)
b = a.set_index(['c', 'd'])
print(b)
c = b['a']
print(c, type(c))
print(c['one']['j'])  # 取复合索引的单个值
print(c['one'])  # 取复合索引的Series值

print('*' * 100)
d = a.set_index(['d', 'c'])['a']
print(d)
print(d.swaplevel())  # 颠倒两个索引的先后顺序
print(d.swaplevel()['one'])  # one为第一列索引,取one值

print('*' * 100)
print(b, type(b))
print(b.loc['one'].loc['h'], type(b.loc['one'].loc['h']))  # 不加loc的话one会被识别为columns
print(b.loc['one', 'h'], type(b.loc['one', 'h']))  # 也可以取到

print('*' * 100 + '时间序列')
# 时间序列
print(pd.date_range(start='20171230', end='20180131', freq='D'))  # 以一天为间隔,生成时间
print(pd.date_range(start='2017-12-30', end='20180131', freq='10D'))  # 以十天为间隔,生成时间
print(pd.date_range(start='2017/12/30', periods=10, freq='10D'))  # 以十天为间隔,生成十个时间
print(pd.date_range(start='20171230', periods=10, freq='2H'))  # 以十天为间隔,生成十个时间
# D天 B工作日 H小时 M每月最后一个日历日
# df['timeStamp'] = pd.to_datetime(df['timeStamp'], format='')  # format大多数情况下不需要写
# resample实现频率转化
# strftime转化时间格式,如 time.strftime('%Y-%m-%d')

