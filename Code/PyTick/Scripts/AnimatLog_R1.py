# -*- coding:utf-8 -*-
'''
    日志处理模块
    Reference:
    [1]nested pie chartshttps://matplotlib.org/3.2.0/gallery/pie_and_polar_charts/nested_pie.html#sphx-glr-gallery-pie-and-polar-charts-nested-pie-py
    [2]pie https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html
    [3]中文显示乱码https://www.jianshu.com/p/b5138e48fefa
    [4]embedin pyqt https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html?highlight=pyqt
    [5]https://www.learnpyqt.com/courses/graphics-plotting/plotting-matplotlib/
'''

from datetime import datetime
from numpy import random
import os
import sys
from PyQt5.QtGui import *  # (the example applies equally well to PySide)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import(
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class LogMoudle(QWidget):
    logDetailList = list()

    def __init__(self, logpath):
         # check file
        super().__init__()
        self.logpath = logpath
        self.__GenList__()
        fileflag = os.path.exists(logpath)
        self.setupUI()
        self.StaticDrawPie()
        self.time_01 = QTimer()

    def setupUI(self):
        mainlayout = QVBoxLayout()
        self.staticPieCanvas = FigureCanvas(Figure(figsize=(5, 5), dpi=100))
        self.danamicPieCanvas = FigureCanvas(Figure(figsize=(5, 5)))
        mainlayout.addWidget(self.staticPieCanvas)
        self.button_1 = QPushButton("Draw")
        self.button_1.clicked.connect(self.StaticDrawPie)
        # mainlayout.addWidget(self.button_1)
        self.setLayout(mainlayout)

    def __GenList__(self):
        try:
            with open(self.logpath, 'r', encoding='utf-8') as f:
                logDetail = f.readlines()
                f.close()
            for i in logDetail:
                deTemp = i.rstrip('\n')
                deTemp = deTemp.split('|')
                if len(deTemp) == 4:
                    CowOne = datetime.strptime(
                        deTemp[0], "%Y-%m-%d %H:%M:%S")
                    CowTwo = datetime.strptime(
                        deTemp[1], "%Y-%m-%d %H:%M:%S")
                    CowThree = int(deTemp[2])
                    deTemp[0] = CowOne
                    deTemp[1] = CowTwo
                    deTemp[2] = CowThree
                    self.logDetailList.append(deTemp)
        except:
            self.logDetailList = ['error' for i in range(4)]

    def StaticDrawPie(self):
        if len(self.logDetailList) > 1:
            self.sPieDraw = self.staticPieCanvas.figure.subplots()
            dayGap = list()
            labels = list()
            for i in self.logDetailList:
                dayGap.append(i[2])
                labels.append(i[3])
            # dayGap = dayGap[0:10]
            dayGap = random.randint(1, 10, size=10)
            labels = labels[0:10]
            self.sPieDraw.pie(dayGap, labels=labels, radius=1, wedgeprops=dict(
                width=0.4, edgecolor='w'))
            self.sPieDraw.pie(dayGap, counterclock=False, radius=1-0.3, wedgeprops=dict(
                width=0.3, edgecolor='w'))
        else:
            labels = ('1', '2', '3', '4')
            self.sPieDraw = self.staticPieCanvas.figure.subplots()
            self.sPieDraw.pie([1, 2, 3, 4], labels=labels)
        self.staticPieCanvas.draw()

    def DynamicDrawPie(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LogMoudle(r'D:\Codes\Python_M\Code\PyTick\Logs\log2.txt')
    ex.show()
    sys.exit(app.exec_())
    # pyqtgraph.examples.run()
