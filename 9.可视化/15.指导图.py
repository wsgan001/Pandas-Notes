# coding=utf-8
"""引导图用于视觉评估统计量的不确定性，例如平均值，中值，中等等。
从数据集中选择指定大小的随机子集，为该子集计算所讨论的统计量，并且过程为 重复指定次数。 
结果图和直方图构成引导图。"""
from pandas.plotting import bootstrap_plot
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
data = pd.Series(np.random.rand(1000))
bootstrap_plot(data)
