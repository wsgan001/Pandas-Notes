# coding=utf-8
from pandas.plotting import andrews_curves
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('./iris.csv')
andrews_curves(data, 'Name')
plt.show()
