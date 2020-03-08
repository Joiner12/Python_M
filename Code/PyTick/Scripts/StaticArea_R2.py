# -*- coding:utf-8 -*-

'''
    直接调用Pyplot生成图片保存然后进行图片显示
    Ref:
    [1] QLabel自适应大小
    https://blog.csdn.net/emdfans/article/details/52936637?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
'''
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import re
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class StaticsArea(QWidget):
    def __init__(self):
        super().__init__()
        # 环境配置
        if False:
            self.srcpath = r"D:\Python_M\Code\PyTick\Src"
            self.logpath = r"D:\Python_M\Code\PyTick\Log"
        else:
            self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
            self.logpath = r"D:\Codes\Python_M\Code\PyTick\Logs"

        self.drawCnt = 0
        self.initUI()

    # 初始化UI界面
    def initUI(self):
        # 整体垂直布局
        mainLayout = QVBoxLayout()
        # 按钮区域布局
        buttonLayout = QHBoxLayout()
        # 绘图按钮
        self.button_1 = QPushButton("Check")
        self.button_1.clicked.connect(self.ChangeFig)

        # 垂直区域显示
        self.FigLabel = QLabel(self)
        self.CurPix = QPixmap(os.path.join(self.srcpath, r"Suya.gif"))

        self.FigLabel.setAlignment(Qt.AlignCenter)
        self.FigLabel.setPixmap(self.CurPix)
        self.FigLabel.setScaledContents(True)

        self.button_2 = QPushButton('Start', self)
        self.button_3 = QPushButton('Stop', self)

        self.button_2.clicked.connect(self.run)
        self.button_3.clicked.connect(self.run)

        # 垂直布局区域
        mainLayout.addWidget(self.FigLabel)
        mainLayout.addLayout(buttonLayout)

        # 设置垂直区域布局
        mainLayout.setStretch(0, 9)
        mainLayout.setStretch(1, 1)
        self.setLayout(mainLayout)

        # 添加水平区域按钮
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.button_1)
        buttonLayout.addWidget(self.button_2)
        buttonLayout.addWidget(self.button_3)

        # 延时显示定时器
        self.delayTim = QTimer()
        self.delayTim.timeout.connect(self.FreImg)

    def run(self):
        movie = QMovie(os.path.join(self.srcpath, r"Suya.gif"))
        self.FigLabel.setMovie(movie)
        if self.sender() == self.button_2:
            movie.start()
        else:
            movie.stop()
            self.FigLabel.setPixmap(self.CurPix)
    # 日志文本进行分析处理

    def __handleDetial__(self):
        # D:\Codes\Python_M\Code\PyTick\Logs
        allLines = ""
        self.detail = list()
        self.duration = list()
        with open(os.path.join(self.logpath, r"log.txt"), encoding='utf-8') as f:
            allLines = f.readlines()
            f.close()

        for i in allLines:
            if i.strip() != "":
                a = re.split(r'[|,\n]', i)
                self.duration.append(int(a[2]))
                self.detail.append(a[3])

    def __drawBar__(self):
        self.CurPix = QPixmap(os.path.join(self.srcpath, r"his-1.png"))
        return
        # 中文字体设置
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.__handleDetial__()
        if len(self.detail) == len(self.duration) and len(self.detail) > 0:
            self.duration
            fig1, ax = plt.subplots()
            x = np.linspace(1, 10, 10)
            ax.bar(self.detail[1:10], self.duration[1:10])
            plt.savefig(os.path.join(self.srcpath, r"bar-1.jpg"), format='png', bbox_inches='tight',
                        transparent=True, dpi=600)  # bbox_inches='tight' 图片边界空白紧致, 背景透明

    def __drawPie__(self):
        # 中文字体设置
        self.CurPix = QPixmap(os.path.join(self.srcpath, r"dolphin-1.jpg"))
        return
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.__handleDetial__()
        if len(self.detail) == len(self.duration) and len(self.detail) > 0:
            fig1, ax = plt.subplots()
            ax.set_facecolor('#eafff5')
            explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)
            ax.pie(self.duration[1:10],
                   labels=self.detail[1:10], explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
            plt.savefig(os.path.join(self.srcpath, r"pie-1.png"), format='png', bbox_inches='tight',
                        transparent=True, dpi=600)  # bbox_inches='tight' 图片边界空白紧致, 背景透明

    def FreImg(self):
        print('delay')
        # self.delayTim.stop()
        self.FigLabel.setPixmap(self.CurPix)

    def ChangeFig(self):
        self.drawCnt = self.drawCnt + 1
        # self.delayTim.start(2000)
        if self.drawCnt % 2 == 0:
            self.__drawPie__()
        else:
            self.__drawBar__()
        self.FigLabel.setPixmap(QPixmap(""))
        self.FigLabel.setPixmap(self.CurPix)
        print(self.CurPix)


class StaticsArea_1(QWidget):
    def __init__(self):
        super().__init__()
        # 环境配置
        if False:
            self.srcpath = r"D:\Python_M\Code\PyTick\Src"
            self.logpath = r"D:\Python_M\Code\PyTick\Log"
        else:
            self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
            self.logpath = r"D:\Codes\Python_M\Code\PyTick\Logs"

        self.drawCnt = 0
        self.initUI()

    # 初始化UI界面
    def initUI(self):
        # 整体垂直布局
        mainLayout = QVBoxLayout()
        # 按钮区域布局
        buttonLayout = QHBoxLayout()
        # 绘图按钮
        self.button_1 = QPushButton("Check")
        self.button_1.clicked.connect(self.ChangeFig)

        # 垂直区域显示
        self.FigLabel = QLabel(self)
        self.CurPix = QPixmap(os.path.join(self.srcpath, r"dolphin-1.jpg"))

        self.FigLabel.setAlignment(Qt.AlignCenter)
        self.FigLabel.setPixmap(self.CurPix)
        self.FigLabel.setScaledContents(True)

        # 垂直布局区域
        mainLayout.addWidget(self.FigLabel)
        mainLayout.addLayout(buttonLayout)

        # 设置垂直区域布局
        mainLayout.setStretch(0, 9)
        mainLayout.setStretch(1, 1)
        self.setLayout(mainLayout)

        # 添加水平区域按钮
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.button_1)

    def ChangeFig(self):
        self.drawCnt = self.drawCnt + 1
        # self.delayTim.start(2000)
        if self.drawCnt % 2 == 0:
            self.CurPix = QPixmap(os.path.join(self.srcpath, r"dolphin-1.jpg"))
        else:
            self.CurPix = QPixmap(os.path.join(self.srcpath, r"his-1.jpg"))
        self.FigLabel.setPixmap(self.CurPix)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ex = StaticsArea()
    ex = StaticsArea_1()
    ex.show()
    sys.exit(app.exec_())
