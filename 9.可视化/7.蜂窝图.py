# coding=utf-8
"""df.plot.hexbin()"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
matplotlib.style.use('ggplot')

df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] += np.arange(1000)

# 一般蜂窝图
df.plot.hexbin(x='a', y='b', gridsize=25)

# 参数C, reduce_C_function: C指定每个（x，y）点处的值, reduce_C_function是将一个bin中的所有值都减少为一个数的一个参数的函数
