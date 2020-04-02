# -*- coding:utf-8 -*-
'''
    日志处理模块
    Reference:
    [1]nested pie chartshttps://matplotlib.org/3.2.0/gallery/pie_and_polar_charts/nested_pie.html#sphx-glr-gallery-pie-and-polar-charts-nested-pie-py
    [2]pie https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html
    [3]中文显示乱码https://www.jianshu.com/p/b5138e48fefa
    [4]embedin pyqt https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html?highlight=pyqt
    [5]https://www.learnpyqt.com/courses/graphics-plotting/plotting-matplotlib/
    [6]PyQt与Matplotlib画图结合 https://blog.csdn.net/The_Time_Runner/article/details/89312660
'''

import PathManager as pathm
from datetime import datetime
from numpy import random, arange, sin, deg2rad, sign, cos, sinc, linspace
import os
import sys
from PyQt5.QtGui import *  # (the example applies equally well to PySide)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import(
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class LogMoudle(QWidget):
    srcpath = pathm.GetUiPath()
    logDetailList = list()
    todayDetailList = list()
    pushStyle_1 = ("QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(2, 9, 34);}"
                   "QPushButton{border:2px solid rgb(118,154,40);}"
                   "QPushButton:hover{background:rgb(118,154,40);}"
                   "QPushButton{background:rgb(127,119,127);}")

    def __init__(self, logpath):
         # check file
        super().__init__()
        self.logpath = logpath
        fileflag = os.path.exists(logpath)
        self.setupUI()
        self.__showImg__()
        self.time_01 = QTimer()

    def setupUI(self):
        mainlayout = QVBoxLayout()
        self.staticPieCanvas = FigureCanvas(Figure(figsize=(6, 4), dpi=100))
        self.staticPieCanvas.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainlayout.addWidget(self.staticPieCanvas)
        butlayout = QHBoxLayout()
        self.button_1 = QPushButton("Draw")
        self.button_2 = QPushButton("Today")
        self.button_3 = QPushButton("Clf")
        self.button_1.setStyleSheet(self.pushStyle_1)
        self.button_2.setStyleSheet(self.pushStyle_1)
        self.button_3.setStyleSheet(self.pushStyle_1)

        mainlayout.addLayout(butlayout)
        butlayout.addWidget(self.button_1)
        butlayout.addWidget(self.button_2)
        butlayout.addWidget(self.button_3)

        self.setLayout(mainlayout)
        self.setStyleSheet("border:1px solid #eaeaea;border-radius:12px;")

        self.button_1.clicked.connect(self.StaticDrawPie_R2)
        self.button_2.clicked.connect(self.drawToday)
        self.button_3.clicked.connect(self.__clf__)

    def __GenList__(self):
        self.logDetailList = list()
        self.todayDetailList = list()
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
                    # today
                    dateToday = datetime.today()
                    today_detail = [dateToday.month, dateToday.day]
                    cowOne_detail = [CowOne.month, CowOne.day]
                    CowTwo_detail = [CowTwo.month, CowTwo.day]
                    if today_detail == cowOne_detail == CowTwo_detail:
                        self.todayDetailList.append(deTemp)
        except:
            self.logDetailList = ['error' for i in range(4)]

    def StaticDrawPie_R2(self):
        # 获取数据列表
        self.__GenList__()
        # canvaes 对象
        self.staticPieCanvas.figure.clf()
        self.sPieDraw = self.staticPieCanvas.figure.subplots()
        # today list data
        if len(self.todayDetailList) > 0:
            things = list()
            duration = list()
            whenDo = list()
            # 合并重复的内容
            for i in self.todayDetailList:
                if i[3] in things:
                    temp_index = things.index(i[3])
                    duration[temp_index] += int(i[2])
                else:
                    things.append(i[3])
                    duration.append(int(i[2]))
                    whenDo.append(i[0].strftime("%H:%M") +
                                  "-"+i[1].strftime("%H:%M"))

            wedges, text = self.sPieDraw.pie(duration, labels=things,
                                             wedgeprops=dict(width=0.3, edgecolor='w'), startangle=90, counterclock=False)

        # box style
        bbox_props = dict(lw=0.72)
        kw = dict(arrowprops=dict(
            arrowstyle='-['), bbox=bbox_props, va="center")

        # 设置pie属性
        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2 + p.theta1
            x = cos(deg2rad(ang))
            y = sin(deg2rad(ang))
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            horizontalalignment = {-1: "right", 1: "left"}[int(sign(x))]
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            self.sPieDraw.annotate(duration[i], xy=(x, y), xytext=(1.35*sign(x), 1.4*y),
                                   horizontalalignment=horizontalalignment, **kw)

        self.sPieDraw.set_title(
            datetime.strftime(datetime.today(), "%Y-%m-%d"))
        self.staticPieCanvas.setStyleSheet("background-color:transparent;")
        self.staticPieCanvas.figure.canvas.draw()

    def drawToday(self):
        self.__GenList__()
        self.staticPieCanvas.figure.clf()
        ax = self.staticPieCanvas.figure.subplots()
        # Example data
        if len(self.todayDetailList) > 0:
            things = list()
            duration = list()
            whenDo = list()
            for i in self.todayDetailList:
                things.append(i[3])
                duration.append(int(i[2]))
                whenDo.append(i[0].strftime("%H:%M") + i[1].strftime("%H:%M"))
            x_pos = arange(len(things))

            ax.bar(x_pos, duration, align='center')
            ax.set_xticklabels(things)

            # ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_ylabel('Performance')
            ax.set_title('How fast do you want to go today?')
            self.staticPieCanvas.setStyleSheet("background-color:transparent;")
            self.staticPieCanvas.figure.canvas.draw()
        else:

            self.__showImg__()

    def __clf__(self):
        self.staticPieCanvas.figure.clf()
        self.__showImg__()
        self.staticPieCanvas.figure.canvas.draw()

       # show image
    def __showImg__(self):
        self.staticPieCanvas.figure.clf()
        ax = self.staticPieCanvas.figure.subplots()
        if False:
            with cbook.get_sample_data(os.path.join(self.srcpath, 'horse.png')) as image_file:
                image = plt.imread(image_file)
            ax.imshow(image)

        # 改变为sinc
        x = linspace(0, 3.14*2, num=100)
        y = sinc(x)
        ax.plot(x, y, marker='o', linewidth=2, markersize=3)
        ax.axis('off')  # clear x-axis and y-axis
        self.staticPieCanvas.setStyleSheet("background-color:transparent;")
        self.staticPieCanvas.figure.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if True:
        ex = LogMoudle(pathm.GetLogFile())
        ex.show()
    sys.exit(app.exec_())
    # pyqtgraph.examples.run()
