# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.style.use('ggplot')

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# 一般面积图
df.plot.area()
plt.show()
# 不堆叠
df.plot.area(stacked=False)
plt.show()
