# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.style.use('ggplot')
ser = pd.Series(np.random.randn(1000))
ser.plot.kde()
plt.show()