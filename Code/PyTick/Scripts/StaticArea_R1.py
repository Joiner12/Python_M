# -*- coding:utf-8 -*-
'''
    统计分析功能区
    [1]文件是否存在https://www.cnblogs.com/jhao/p/7243043.html
    [2]将 matplotlib 嵌入 PyQt5 https://zhuanlan.zhihu.com/p/26379590
    [3]透明背景https://blog.csdn.net/hfut_jf/article/details/52648033
    [4]python中plt.hist参数详解 https://www.cnblogs.com/python-life/articles/6084059.html
    [5]pie https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html
    [6]re.split https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p01_split_string_on_multiple_delimiters.html
'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.cbook as cbook
import sys
import os
import re
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# matlab lib
import matplotlib
matplotlib.use('Qt5Agg')

# 将pyplot嵌入到GUI中


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
        # 初步提取之后的日志

        self.logOrg = ""
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

        # 中文字体设置
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # matlab图窗
        self.figure_1 = plt.figure()
        self.canvas_1 = FigureCanvas(self.figure_1)

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
        self.__handleDetial__()
        if len(self.detail) == len(self.duration) and len(self.detail) > 0:
            self.figure_1.clf()
            self.duration
            ax = self.figure_1.subplots()
            x = np.linspace(1, 10, 10)
            ax.bar(self.detail[1:10], self.duration[1:10])
            self.canvas_1.draw()

    def __drawPie__(self):
        self.__handleDetial__()
        if len(self.detail) == len(self.duration) and len(self.detail) > 0:
            self.figure_1.clf()
            ax = self.figure_1.subplots()
            ax.set_facecolor('#eafff5')
            explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)
            ax.pie(self.duration[1:10],
                   labels=self.detail[1:10], explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
            self.canvas_1.draw()

    # show image
    def __showImg__(self):
        self.figure_1.clf()
        ax = self.figure_1.subplots()
        with cbook.get_sample_data(os.path.join(self.srcpath, 'love.png')) as image_file:
            image = plt.imread(image_file)
        ax.imshow(image)
        ax.axis('off')  # clear x-axis and y-axis
        self.canvas_1.draw()

    def ChangeFig(self):
        self.drawCnt = self.drawCnt + 1
        if self.drawCnt % 3 == 0:
            self.__showImg__()
        elif self.drawCnt % 3 == 1:
            self.__drawPie__()
        else:
            self.__drawBar__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StaticsArea()
    ex.show()
    sys.exit(app.exec_())
