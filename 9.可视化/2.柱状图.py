# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
matplotlib.style.use('ggplot')

plt.figure()
np.random.seed(123456)
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()  # 第i个元素为前i个的和
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()

# df.plot.bar()
# 单个条形图
df.iloc[5].plot.bar()
plt.axhline(0, color='k')
plt.show()

# 多个条形图
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar()
plt.show()

# 堆叠的条形图
df2.plot.bar(stacked=True)
plt.show()

# 水平条形图
df2.plot.barh(stacked=True)
plt.show()
