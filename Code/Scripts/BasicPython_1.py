#!/bin/usr/env/ python3 → Linux/OS X系统下使用
# -*- coding:utf-8 -*-
# coding:utf-8 表示计算机以utf-8格式打开源文件

'''
    python 基本数据和数据结构
    [1]字符串和编码https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

'''
from types import MethodType
import numpy as np


def Variables():
    # 多变量赋值
    a, b, c = 1, 2, 'join'
    del a
    d = 1e-3
    debug_a = 'True'
    # 格式化输出
    print('%s,%d,%0.2f' % ('this', 2, 1.0))


def HandleList():
    # index starts from 0
    a = ['Bob', 'Jen', 'Alin']
    for i in a:
        print(i)
    a.append('Hellen')
    a.append({'Youger', 'Tangle'})
    a.pop()
    a.pop(1)
    debug_a = 'True'


def HandleInput():
    promote_1 = input('输入:')
    if int(promote_1) > 100:
        print('它比100大\n')
    elif int(promote_1) < 10:
        print('它比10小\n')
    else:
        print('它啥都不是\n')


def HandleLoop():
    circle = 10
    while circle > 3:
        print(circle)
        circle = circle-1


def HandleDict():
    dic_1 = {'what': 1, 'the': 2, 'fuck': 3}
    for i in dic_1:
        print('key:%s\t value:%s\n' % (i, dic_1[i]))
    isinstance(dic_1, dict)

    # key是不可变对象( vs可变对象)
    a = 'dacv' in dic_1
    dic_1.pop('what')
    b = dic_1.get('what', -100)
    c = dic_1.get('the')
    debug_1 = 0


def HandleSet():
    s = set([1, 2, 3])
    s.remove(2)
    s.add(4)
    debug_a = 0


def Rfunction():
    # 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
    a_r = abs
    a_r(-1)
    print()


def HandleCheckPara(a):
    if not isinstance(a, (int, float)):
        print('argument check failed')
        return
    else:
        print('argument check succeed')


'''
    object oriented programming 
'''


class Ai():
    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(self.name)


def SetAge(self, age):
    self.age = age
    print('give it a new method')


def TestMethod():
    ai = Ai('hrt')
    ai.SetAge = MethodType(SetAge, ai)
    ai.SetAge(3)


def SecondArray():
    a = [0 for i in range(3)]
    b = [[a] for i in range(3)]
    a = np.linspace(0, 11, 12, dtype=int)
    a_1 = a.reshape(2, 6)
    debug_a = 0

    # 利用句柄进行操作
    b_1 = [[1, 2, 3], [5, 3], [7, 6, 3, 2]]
    for i in b_1:
        for j in i:
            print(j)


if __name__ == "__main__":
    # SecondArray()
    a = 3
    b = a**2
    c = a*2
    debug_a = 0
