#-*- coding:utf-8 -*-
"""
    https://zhuanlan.zhihu.com/p/21775104
"""

from scipy.integrate import odeint
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation 


def lorez(w,t,p,r,b):
    x,y,z = w
    return np.array([p*(y-x),x*(r-z),x*y-b*z])

t = np.arange(0,100,0.01)
#ode求解微分方程
track1 = odeint(lorez,(0,1,0.1),t,args=(10.0,30.0,3.0))


fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track1[:,0],track1[:,1],track1[:,2],'b', markersize=8)
# ax.plot(track1[0,:],track1[1,:],track1[2,:],'b', markersize=8)
line1=ax.plot([],[],'b:')#初始化数据，line是估计，point是轨迹的头部

point1=ax.plot([],[],'bo',markersize=10)

line2=ax.plot([],[],'r:')

point2=ax.plot([],[],'ro',markersize=10)

images=[]


def init():#该函数用于初始化动画
    line1=ax.plot([],[],'b:',markersize=8)
    point1=ax.plot([],[],'bo',markersize=10)
    line2=ax.plot([],[],'r:',markersize=8)
    point2 = ax.plot([], [], 'ro', markersize=10)
    return line1,point1,line2,point2
                     
def anmi(i):#anmi函数用于每一帧的数据更新，i是帧数。
    ax.clear()
    line1=ax.plot(track1[0:10*i,0],track1[0:10*i,1],track1[0:10*i,2],'b:', markersize=8)
    point1 = ax.plot(track1[10*i-1:10*i,0],track1[10*i-1:10*i,1],track1[10*i-1:10*i,2],'bo', markersize=10)
    line2 = ax.plot(track2[0:10*i, 0], track2[0:10*i, 1], track2[0:10*i, 2], 'r:',markersize=8)
    point2 = ax.plot(track2[10*i-1:10 * i, 0], track2[10*i-1:10 * i, 1], track2[10*i-1:10 * i, 2], 'ro', markersize=10)
    return line1,point1,line2,point2

#animation.FuncAnimation用于动画制作，输入init函数和anmi函数，frams是帧数，一共画500祯，interval是相邻祯的间隔，单位是毫秒，此处为2毫秒
anim = animation.FuncAnimation(fig, anmi, init_func=init,
                              frames=500, interval=2, blit=False,repeat=False)
