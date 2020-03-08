# -*- utf-8 -*-
'''
    字符串分隔
'''

import os
import re


def SplitInfo():
    allLines = ""
    detail = list()
    duration = list()
    file = r'D:\Codes\Python_M\Code\PyTick\Logs\log - 副本.txt'

    with open(file, encoding='utf-8') as f:
        allLines = f.readlines()
        f.close()
    for i in allLines:
        if i.strip() != "":
            print(i)
            a = re.split(r'[|,\n]', i)
            duration.append(int(a[2]))
            detail.append(a[3])
            print(a[2], a[3])
    DetDuration = dict(zip(detail, (duration)))
    print(DetDuration.keys)
    print(DetDuration.values)


if __name__ == "__main__":
    # if ~False:
    #     print("false")
    # SplitInfo()
    a = False
    while True:
        a = not a
        print(a)
