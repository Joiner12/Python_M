#coding:utf-8

__author__: "Risky"
__date__: "2019-12-2"
import re
import matplotlib.pyplot as plt
import numpy as np
import math

# 从单个文件中读取
def GetLrc():
    print('get lrc from file')
    file = 'D:\\1874 (Live).lrc'
    with open(file,"r",encoding="utf-8") as lrc:
        lrd_detail = lrc.readlines()
        print('lrc file open succeed')
    for piece_lrc in lrd_detail:
        piece_pattern = re.compile(r"\[.+\]")
        # print('origin:'+ piece_lrc)
        words = piece_pattern.sub(" ",piece_lrc)
        if len(words)!=0:
            print(words)
        
    lrc.close()

def Figureplot():
    data = np.arange(10)
    print(data) 
    plt.plot(data,data)
    print('last line')
    plt.show()


def plot_2():

    x=[0,1,2,3,4,5,6,7,8,9]
    y=[12,23,4,10,22,33,44,23,35,7]
    plt.bar(x,y,align='center',alpha=0.5)
    plt.xticks(x,x)
    plt.ylabel('count')
    plt.title('Distribution')
    plt.show()

    

if __name__ == '__main__':
    GetLrc()
    # Figureplot()    
    # plot_2()
  
    