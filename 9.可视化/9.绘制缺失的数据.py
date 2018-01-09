# coding=utf-8
"""pandas会自动处理缺失值, 根据图形的不同,做丢弃, 自动填充, 遗漏处理
图	            缺失值处理
Line	        Leave gaps at NaNs
Line(stacked)	Fill 0’s
Bar	            Fill 0’s
Scatter	        Drop NaNs
Histogram	    Drop NaNs (column-wise)
Box	            Drop NaNs (column-wise)
Area	        Fill 0’s
KDE	            Drop NaNs (column-wise)
Hexbin	        Drop NaNs
Pie	            Fill 0’s
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
matplotlib.style.use('ggplot')

