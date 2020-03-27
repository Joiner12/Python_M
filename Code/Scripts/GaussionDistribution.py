# -*- coding: utf-8 -*-
'''
    Normal(Gaussion) Distribution
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(0,10,num=101)
y1 = norm.pdf(x,5,1)

# 手动计算正态分布
mu = 5
sigma = 1

y_sig = np.exp(-(x - mu) ** 2 /(2* sigma **2))/(np.sqrt(2*np.pi)*sigma)

fig1 = plt.figure()
axes = fig1.add_subplot(111)
axes.plot(x,y1)
axes.set_title('normal distribution')

fig2,axes_2 = plt.subplots(2,1)
axes_2[0].plot(x,y_sig)



