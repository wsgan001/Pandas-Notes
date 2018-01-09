# coding=utf-8
"""df.plot.hist, df.hist"""
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.random.seed(123456)
matplotlib.style.use('ggplot')

df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                    'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
# 普通直方图
df4.plot.hist(alpha=.5)
plt.show()

# 堆叠直方图
df4.plot.hist(stacked=True, bins=20)  # bins控制bin size
plt.show()

# 水平直方图
df4.plot.hist(orientation='horizontal')
plt.show()

# 累计直方图
df4.plot.hist(cumulative=True)
plt.show()

# 多个子图 df.hist()
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
# df.diff series.diff 差分
df['A'].diff().hist()
plt.show()
df.diff().hist(color='k', bins=50)
plt.show()
# # by参数绘制分组的直方图: 将data的值依个分类, 按类别绘制直方图
data = pd.Series(np.random.randn(1000))
data.hist()
plt.show()
data.hist(by=np.random.randint(4, 10, 1000))
plt.show()
