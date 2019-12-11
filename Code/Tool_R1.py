# !usr/bin/python3
# encoding:utf-8

import datetime
from PyQt5 import QtWidgets
import os
import random

def StuckIn():
    now = datetime.datetime.now()
    time_now = now.strftime('%a, %b %d %H:%M')
    a = datetime.datetime.now()
    cnt = 0
    while True:
        b = datetime.datetime.now()
        dura = b - a
        
        if (dura.seconds//1) == 1:
            a = b
            for i in range(1,random.randint(1,5),1):
                print("...",end="")
            # print(a.strftime('%H:%M:%S'))
            print("stranded in situ!",end="")
            a_1 = random.randint(0,9)
            b_1 = "%d"%a_1
            colr = "color " + b_1
            os.system(colr)
            
            cnt += 1
            if cnt == 3:
                cnt = 0
                print("")
                os.system("cls")

if __name__ =="__main__":
   StuckIn()