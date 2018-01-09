# coding=utf-8
"""df.plot.pie(), series.plot.pie()"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
matplotlib.style.use('ggplot')
series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
# 一般饼图
series.plot.pie()
plt.show()

# 对于DataFrame, 要么指定column, 要么设定subplots为True(这样会绘制所有columns)
df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
df.plot.pie(subplots=True)
plt.show()

# labels参数, colors参数... 凡是matplotlib.pyplot.pie()支持的参数都可以
series.plot.pie(labels=list('abcd'), colors=list('rbyw'), autopct='%.2f')
plt.show()

# 如果数据加和小于1, 则绘制半圆
pd.Series([0.1]*8).plot.pie(title='1')
plt.show()
