# coding=utf-8
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
# 一般散点图矩阵
scatter_matrix(df)
plt.show()

# diagonal参数:指定对角的图类型
scatter_matrix(df, diagonal='kde')

# 