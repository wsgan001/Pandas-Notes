# coding=utf-8
"""series.plot.box(), dataframe.plot.box(), dataframe.boxplot()"""
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.random.seed(123456)
matplotlib.style.use('ggplot')

df = pd.DataFrame(np.random.randn(10, 5), columns=list('ABCDE'))
# 最简单的箱型图
df.plot.box()
plt.show()

# 自定义箱型图的颜色(boxes, whiskers, medians, caps)
color = dict(boxes='Blue', whiskers='Orange', medians='DarkBlue', caps='Gray')
# # sym: 异常值标记
df.plot.box(color=color, sym='r*')
plt.show()

# 通过传递matplotlib的boxplot的参数vert来绘制水平箱型图. positions参数来(干嘛) TODO
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])
plt.show()

# df.boxplot
df.boxplot()
plt.show()

# 传递by参数来创建箱型图组
df = pd.DataFrame(np.random.rand(10, 2), columns=['Col1', 'Col2'])
df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
bp = df.boxplot(by='X')
plt.show()
# # by参数可以是多个列
df['Y'] = pd.Series(['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'])
bp = df.boxplot(by=['X', 'Y'])
plt.show()
