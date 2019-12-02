#coding:utf-8
import re
import matplotlib.pyplot as plt
import numpy as np

# 从单个文件中读取
def GetLrc():
    print('get lrc from file')
    file = 'D:\\1874 (Live).lrc'
    with open(file,"r",encoding="utf-8") as lrc:
        lrd_detail = lrc.readlines()
        print('lrc file open succeed')
    for piece_lrc in lrd_detail:
        print(piece_lrc)
        piece_pattern = re.compile(piece_lrc)
        exp_sub = '^r"[".*?r"]"&'
        if piece_pattern.match(exp_sub):
            print(piece_pattern.findall(exp_sub))

    lrc.close()

def Figureplot():
    print("figure plotting")
    data = np.arange(10)
    print(data) 
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    plt.plot(data,data)
    plt.plot(np.random.randn(50).cumsum(), 'k--')
    print('last line')
    
if __name__ == '__main__':
    # GetLrc()
    Figureplot()    