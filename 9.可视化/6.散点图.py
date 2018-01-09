# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
matplotlib.style.use('ggplot')
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
# 一般散点图
df.plot.scatter(x='a', y='b')
plt.show()

# ax
ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group1')
ax2 = df.plot.scatter(x='a', y='c', color='Pink', label='Group3')
df.plot.scatter(x='c', y='d', color='Blue', label='Group2', ax=ax)
df.plot.scatter(x='a', y='d', color='Yellow', label='Group2', ax=ax2)
plt.show()

# c: 可以将关键字c给出为列的名称，为每个点提供颜色
df.plot.scatter(x='a', y='b', c='c', s=50)
plt.show()

# 传递matplotlib scatter支持的参数,如气泡尺寸s
df.plot.scatter(x='a', y='b', s=df['c']*200)
plt.show()

