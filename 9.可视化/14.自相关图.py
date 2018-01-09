# coding=utf-8
"""自相关图通常用于检查时间序列的随机性。这是通过在不同的时间滞后的数据值进行计算自相关函数。
如果时间序列是随机的，这样应该接近零自相关的任何和所有时间的分离。
如果时间序列是非随机的那一个或一个以上的相关性将显著非零。图中显示的水平线对应95%和99%个置信带。虚线为99%置信带。"""
from pandas.plotting import autocorrelation_plot
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

data = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(np.linspace(-9 * np.pi, 9 * np.pi, num=1000)))
autocorrelation_plot(data)