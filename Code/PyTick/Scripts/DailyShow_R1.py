# -*- codidng: -*-
'''
    daily list
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
import os 
import sys
from numpy import random

class Daily(QWidget):
    
    bgTimer = QTimer()
    def __init__(self):
        super().__init__()
        self.setGeometry(-1080,200,500,20)
        self.bgTimer.start(1000)
        self.bgTimer.timeout.connect(self.paintEvent_R1)
        self.setWindowTitle("color")


    def setupUI(self):
        print("setup ui")

    def paintEvent_R1(self):
        self.palette1 = QPalette()
        r = random.randint(0,255,size=1)
        g = random.randint(0,255,size=1)
        b = random.randint(0,255,size=1)
        self.palette1.setColor(self.backgroundRole(), QColor(r, g, b))   # 设置背景颜色
        self.setPalette(self.palette1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Daily()
    ex.show()
    sys.exit(app.exec_())