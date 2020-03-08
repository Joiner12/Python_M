# -*- coding:utf-8 -*-
'''
    scroll text

    Reference:
    [1]QLable介绍https://zhuanlan.zhihu.com/p/32134728
    [2]QLable介绍https://blog.csdn.net/jia666666/article/details/81504595
    [3]QT文字上下滚动https://blog.csdn.net/douzhq/article/details/80891144
    [4]Animation介绍 https://zhuanlan.zhihu.com/p/51690978
    [5]QPropertyAnimation in PyQthttp://zetcode.com/pyqt/qpropertyanimation/
'''
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SrollTxt(QWidget):
    def __init__(self):
        super().__init__()
        print('roll text')
        self.logdetail = 0  # 字符串表
        self.timer_1 = QTimer()
        self.counter = 0
        self.pieceIndex = 0  # 字符串列表指针
        # self.setGeometry(100, 100, 200, 100)
        self.initLabel()
        self.__ReadLog__()
        self.timer_1.timeout.connect(self.HandleText)

        # animation
        self.txtPropAnimation = QPropertyAnimation(self.label_1, b"geometry")
    # 鼠标操作

    def enterEvent(self, event):
        # 读取日志文件并存储
        self.timer_1.start(2000)

    def leaveEvent(self, event):
        self.timer_1.stop()
        self.txtPropAnimation.stop()
        self.label_1.setText("Gausss...")
        self.label_1.adjustSize()

    def HandleText(self):
        # 空表
        if len(self.logdetail) == 0:
            return
        if len(self.logdetail) - 1 < self.pieceIndex:
            self.pieceIndex = 0
        curLine = self.logdetail[len(self.logdetail) - 1 - self.pieceIndex]
        if curLine.strip() != "":
            self.label_1.setText(curLine)

            self.txtPropAnimation.setDuration(500)
            self.label_1.adjustSize()

            self.txtPropAnimation.setStartValue(
                QRect(0, self.label_1.height(), self.width(), self.label_1.height()))
            self.txtPropAnimation.setEndValue(
                QRect(0, 0, self.width(), self.label_1.height()))
            self.label_1.show()
            self.txtPropAnimation.start()
        self.pieceIndex = self.pieceIndex + 1

    def __ReadLog__(self):
        f = open(r"D:\Codes\Python_M\Code\PyTick\Logs\log.txt",
                 'r', encoding='UTF-8')
        allLines = f.readlines()
        self.logdetail = allLines

    def initLabel(self):
        self.label_1 = QLabel(self)
        self.label_1.setStyleSheet(
            "QLabel{color:rgb(100,100,100,250);font-size:20px;font-weight:bold;font-family:Consoles;}")
        self.label_1.setText("Gausss...")
        self.label_1.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SrollTxt()
    ex.show()
    sys.exit(app.exec_())
