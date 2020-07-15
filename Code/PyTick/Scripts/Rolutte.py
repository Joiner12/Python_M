# -*- coding:utf-8 -*-
"""
    Russian Rolutte
"""
from math import sqrt, sin, cos, pi
import numpy as np
from random import random
import PathManager
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class Rolutte(QWidget):
    MaxInt = 2**31
    arrowSet = (1, 0)  # 箭头极坐标
    rotateRad = 10   # 旋转角速度
    pieWedgeSize = 12
    ArrowHeadPos = np.array([])
    randomSeedFlag = False  # 停止随机状态
    randomDelayTime = 0     # 停止延时
    rotateCycles = 0       # 运动圈数

    def __init__(self):
        super().__init__()
        self.timer_1 = QTimer()
        self.timer_2 = QTimer()
        self.setupUI()
        self.show()

        # parameter initialization
        self.OptCnt_1 = 0
        self.setGeometry(100, 500, 400, 400)
        print("Russian Rolutte,Road To God")

    def setupUI(self):
        layout = QVBoxLayout()
        btn_layout = QHBoxLayout()
        self.figure_1 = FigureCanvas(Figure(figsize=(5, 5), facecolor="none"))
        self.btn_1 = QPushButton("EVIL")
        self.btn_2 = QPushButton("GOD")
        self.infoLabel = QLabel("00")
        self.infoLabel.setStyleSheet(
            "QLabel{color:rgb(100,100,100,250);font-size:20px;font-weight:bold;font-family:Consoles;}")

        btn_layout.addWidget(self.btn_1)
        btn_layout.addWidget(self.btn_2)
        btn_layout.addWidget(self.infoLabel)

        self.btn_1.clicked.connect(self.ArrowRotateStart)
        self.timer_1.timeout.connect(self.ArrowRotating)

        self.btn_2.clicked.connect(self.ArrowRotateStop)
        self.timer_2.timeout.connect(self.DelayStop)
        layout.addWidget(self.figure_1, 0)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        self.__initFigure__()

    def __initFigure__(self):
        # 停止延时
        self.randomSeedFlag = False
        self.figure_1.figure.clf()
        ax1 = self.figure_1.figure.subplots()
        # matrix
        i_temp = np.linspace(0, self.pieWedgeSize-1,
                             num=self.pieWedgeSize, dtype=int)
        angle_temp = pi/self.pieWedgeSize + 2*i_temp*pi/self.pieWedgeSize
        pos_temp = np.array([np.cos(angle_temp), np.sin(angle_temp)])
        pos = pos_temp.T
        # data structure [(x,y)]
        self.ArrowHeadPos = pos
        x = [1]*self.pieWedgeSize
        ax1.pie(x, startangle=90, colors='w',
                wedgeprops=dict(edgecolor='k'), radius=sqrt(2))
        ax1.arrow(0, 0, 1, 0, head_width=0.05, head_length=0.1, fc='b', ec='k')
        self.figure_1.figure.canvas.draw()

    def ArrowRotateStart(self):
        self.timer_1.start(50)
        self.randomSeedFlag = True
        self.randomDelayTime = int(random()*10) + 1

    def ArrowRotating(self):
        # cycle
        if int(self.OptCnt_1/12) != self.rotateCycles:
            self.rotateCycles = int(self.OptCnt_1/12)

        if int(self.rotateCycles/2) % 2 == 0:
            cur_index = self.pieWedgeSize - int(self.OptCnt_1 % 12) - 1
        else:
            cur_index = int(self.OptCnt_1 % 12)
        self.UpdateArrowfigure(self.ArrowHeadPos[cur_index])
        print("running", self.OptCnt_1)
        if self.OptCnt_1 > self.MaxInt:
            self.OptCnt_1 = 0
        else:
            self.OptCnt_1 += 1

        self.infoLabel.setText(str(int(self.OptCnt_1 % 100)))

    def ArrowRotateStop(self):
        if not self.randomSeedFlag:
            return
        self.timer_2.start(500)
        if self.timer_1.isActive():
            self.timer_1.stop()

        print("timer stop")
        self.infoLabel.setText("00")

    def DelayStop(self):
        if int(self.OptCnt_1/12) != self.rotateCycles:
            self.rotateCycles = int(self.OptCnt_1/12)

        if int(self.rotateCycles/2) % 2 == 0:
            cur_index = self.pieWedgeSize - int(self.OptCnt_1 % 12) - 1
        else:
            cur_index = int(self.OptCnt_1 % 12)
        self.UpdateArrowfigure(self.ArrowHeadPos[cur_index])
        if self.OptCnt_1 > self.MaxInt:
            self.OptCnt_1 = 0
        else:
            self.OptCnt_1 += 1

        self.randomDelayTime -= 1
        if self.randomDelayTime == 0:
            if self.timer_2.isActive():
                self.timer_2.stop()
            self.randomSeedFlag = False

            proty_1 = "<p style='font-size:20px;color:#ff0000;'>your <br> mom's <br> head</p>"
            reply = QMessageBox.information(
                self, "Rolutte", proty_1, QMessageBox.Yes | QMessageBox.No)

    def UpdateArrowfigure(self, arrowSet=(0, 1)):
        self.figure_1.figure.clf()
        ax = self.figure_1.figure.subplots()
        x = [1]*self.pieWedgeSize
        ax.pie(x, startangle=90, colors='w',
               wedgeprops=dict(edgecolor='k'), radius=sqrt(2))
        x = arrowSet[0]
        y = arrowSet[1]
        ax.arrow(0, 0, x, y, head_width=0.05, head_length=0.1, fc='b', ec='k')
        self.figure_1.figure.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Rolutte()
    sys.exit(app.exec_())
