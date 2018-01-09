# coding=utf-8
"""滞后图用于检查数据集或时间序列是否是随机的。随机数据不应在滞后图中显示任何结构。非随机结构意味着底层数据不是随机的。"""
import numpy as np
import pandas as pd
from pandas.plotting import  lag_plot
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(np.linspace(-99 * np.pi, 99 * np.pi, num=1000)))
lag_plot(data)