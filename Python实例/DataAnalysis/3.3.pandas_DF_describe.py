# coding:utf-8
import pandas as pd

df = pd.read_csv('./dogNames.csv')
print(df.head())
print(df.info())

# DataFrame中排序的方法
df = df.sort_values(by='Count_AnimalName', ascending=False)  # 默认升序
print(df.head(10))


