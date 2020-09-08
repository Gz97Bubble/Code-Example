# coding:utf-8
import numpy as np


def fill_nan_array(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 选择当前的这一列
        nan_num = np.count_nonzero(temp_col != np.nan)
        if nan_num != 0:  # 不为0说明这一列有nan
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前一列不为nan的araay
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()  # 选中当前为nan的位置,赋值为均值
    return t1


if __name__ == '__main__':
    t1 = np.arange(24).reshape(4, 6).astype(float)
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_nan_array(t1)
    print(t1)
