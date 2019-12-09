#coding:utf-8

__author__: "Risky"
__date__: "2019-12-2"

import matplotlib.pyplot as plt
import numpy as np
import math



def Figureplot():
    data = np.arange(10)
    print(data) 
    plt.plot(data,data)
    print('last line')
    plt.show()

'''
    绘图
'''
def plot_2():
    x=[0,1,2,3,4,5,6,7,8,9]
    y=[12,23,4,10,22,33,44,23,35,7]
    plt.bar(x,y,align='center',alpha=0.5)
    plt.xticks(x,x)
    plt.ylabel('count')
    plt.title('Distribution')
    plt.show()

    

if __name__ == '__main__':
    
    # Figureplot()    
    plot_2()
  
    