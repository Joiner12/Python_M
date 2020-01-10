# coding:utf-8
__author__:"Anonymous"

'''
    sigmoid kerl function & figure
'''
import os
import numpy as np
import matplotlib.pyplot as plt

# sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# relu function
def relu(x):
    return np.maximum(0,x)

def TestFunc():
    x1 = np.arange(-10,10,0.1)
    y1 = sigmoid(x1)

    plt.plot(x1,y1)
    plt.show()


if __name__=="__main__":
    os.system("cls")
    os.system("dir")
    print("this is f**k aswsome")
    TestFunc()
    