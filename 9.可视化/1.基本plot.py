# coding=utf-8
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
matplotlib.style.use('ggplot')

# pd.date_range()生成一个时间索引
np.random.seed(123456)
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()  # 第i个元素为前i个的和
ts.plot()
plt.show()

# 默认DF的每一列作为一条线绘制出来
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot()
plt.show()

# 只绘制DF的某一列
df.plot(y='C')
