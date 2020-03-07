# -*- coding:utf-8 -*-
'''
    统计分析功能区
    [1]文件是否存在https://www.cnblogs.com/jhao/p/7243043.html
    [2]将 matplotlib 嵌入 PyQt5 https://zhuanlan.zhihu.com/p/26379590
    [3]透明背景https://blog.csdn.net/hfut_jf/article/details/52648033
    [4]python中plt.hist参数详解 https://www.cnblogs.com/python-life/articles/6084059.html
'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.cbook as cbook
import sys
import os
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# matlab lib
import matplotlib
matplotlib.use('Qt5Agg')


class StaticsArea(QWidget):
    def __init__(self):
        super().__init__()
        # 环境配置
        if False:
            self.srcpath = r"D:\Python_M\Code\PyTick\Src"
            self.logpath = r"D:\Python_M\Code\PyTick\Log"
        else:
            self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
            self.logpath = r"D:\Codes\Python_M\Code\PyTick\Log"

        self.logOrg = ""
        self.initUI()
        self.__ReadLog__()
        self.__drawBar__()

    # 初始化UI界面
    def initUI(self):
        # 整体垂直布局
        mainLayout = QVBoxLayout()
        # 按钮区域布局
        buttonLayout = QHBoxLayout()
        # 绘图按钮
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.button_3 = QPushButton("3")

        # matlab图窗
        self.figure_1 = plt.figure(facecolor="none", edgecolor="none")
        self.canvas_1 = FigureCanvas(self.figure_1)

        self.figure_2 = plt.figure()
        self.canvas_2 = FigureCanvas(self.figure_2)

        # 垂直布局区域
        mainLayout.addWidget(self.canvas_1)
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
        self.setGeometry(100, 100, 500, 500*0.618)
    # draw

    def matdraw(self):
        self.figure_1.clf()
        money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
        ax = self.figure_1.subplots()
        ax.bar([1, 2, 3, 4], money)
        self.canvas_1.draw()

        # 读取日志文本

    def __ReadLog__(self):
        if os.path.exists(os.path.join(self.logpath, r"log.txt")):
            f = open(os.path.join(self.logpath, r"log.txt"),
                     'r', encoding='UTF-8')
            self.logOrg = f.readlines
            f.close()

    # 日志文本进行分析处理
    def __handleDetial__(self):
        pass

    # bar
    def __drawBar__(self):
        self.figure_1.clf()
        money = np.random.randint(1, 10, 10)
        ax = self.figure_1.subplots()
        x = np.linspace(1, 10, 10)
        self.figure_1.subplots_adjust(left=None, bottom=None, right=None, top=None,
                                      wspace=None, hspace=None)
        # ax.hist(np.random.randn(500), bins=50, alpha=0.5)
        ax.bar(x, money)
        ax.axis('off')
        self.canvas_1.draw()

    # pie
    def __drawPie__(self):
        pass

    # show image
    def __showImg__(self):
        self.figure_1.clf()
        ax = self.figure_1.subplots()
        with cbook.get_sample_data(os.path.join(self.srcpath, 'smoking-1.jpg')) as image_file:
            image = plt.imread(image_file)

        ax.imshow(image)
        ax.axis('off')  # clear x-axis and y-axis
        self.canvas_1.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StaticsArea()
    ex.show()
    sys.exit(app.exec_())
