# !usr/bin/python3
# encoding:utf-8

import datetime
from PyQt5.QtCore import Qt,QBasicTimer
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QHBoxLayout, QVBoxLayout,QApplication, QMainWindow)

from PyQt5.QtWidgets import (QPushButton,QProgressBar)

import sys
import os
import random

# generate random dos message show
def StuckIn():
    now = datetime.datetime.now()
    time_now = now.strftime('%a, %b %d %H:%M')
    a = datetime.datetime.now()
    while True:
        b = datetime.datetime.now()
        dura = b - a
        
        if (dura.seconds//1) == 1:
            a = b
            for i in range(1,random.randint(1,5),1):
                print("...",end="")
            # print(a.strftime('%H:%M:%S'))
            print("stranded in situ!",end="")
            b_1 = "%d"%a_1
            colr = "color " + b_1
            os.system(colr)
          
            cnt += 1
            if cnt == 3:
                print("")
                os.system("cls")

# main window
class loveRiver(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # slider in window
        # lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        # processbar
        Pb1 = ProcessBar_1()
        wi = Window_Info()


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        # hbox.addWidget(lcd)
        hbox.addWidget(sld)
        hbox.addWidget(Pb1)
        

        self.setLayout(hbox)
        # sld.valueChanged.connect(lcd.display)
        self.setGeometry(300,300,720,720*0.618)
        self.show()

'''
    菜单|状态|工具
'''
class Window_Info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.menuBar()
        self.statusBar().showMessage('ReadyGo!')
        self.setWindowTitle("Are U OK?")

class ProcessBar_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)
        
        # 按键
        self.btn = QPushButton('THIS IS A BUTTON',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)
        
        self.timer = QBasicTimer()

        self.setGeometry(300,300,600,600*0.618)

        self.setWindowTitle('hah')
        self.show()

    def timerEvent(self,e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('finished')
            return
            
        self.step = self.step + 5
        self.pbar.setValue(self.step)

    
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('START')
        else:
            self.timer.start(100,self)
            self.btn.setText('STOP')



if __name__ =="__main__":
#    StuckIn()
    if False:
        app = QApplication(sys.argv)
        ex = loveRiver()
        sys.exit(app.exec_()) 
    else:
        filepath = os.path.abspath(os.path.join(os.path.abspath(__file__),'../..'))
        print(filepath)