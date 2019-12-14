# !usr/bin/python3
# encoding:utf-8

import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QHBoxLayout, QVBoxLayout,QApplication, QMainWindow)
import sys
import os
import random

# generate random dos message show
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

# main window
class Window_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # slider in window
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        hbox = QHBoxLayout()
        hbox.addWidget(lcd)
        hbox.addWidget(sld)

        self.setLayout(hbox)
        sld.valueChanged.connect(lcd.display)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,400,200)
        self.setWindowTitle("TRY")
        self.show()




if __name__ =="__main__":
#    StuckIn()
    app = QApplication(sys.argv)
    ex = Window_main()
    sys.exit(app.exec_()) 