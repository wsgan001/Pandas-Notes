# coding=utf-8
"""大多数绘图方法都有一组关键字参数来控制返回图形的布局和格式"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.style.use('ggplot')

# 控制图例: legend=False
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot(legend=False)

# scales刻度尺寸: 将x或y log化
ts = np.exp(ts.cumsum())
ts.plot(logy=True)  # 还有logx, loglog

# 两个y轴
df.A.plot()
df.B.plot(secondary_y=True)
plt.show()
# # 为两个y轴添加标签
ax = df.plot(secondary_y=['A', 'B'])
ax.set_ylabel('C D scale')
ax.right_ax.set_ylabel('A B scale')
plt.show()
# # # ax.right_ax.set_ylabel('A B scale')这个操作会默认AB图例有个right, 可以设置参数去掉
df.plot(secondary_y=['A', 'B'], mark_right=False)
plt.show()

# 调整刻度分辨率
df.A.plot(x_compat=True)
plt.show()

# 子图
df.plot(subplots=True)
# # layout参数:设置子图几行几列, sharex: 是否共享x
df.plot(subplots=True, layout=(4, 1), figsize=(6, 6), sharex=False)
