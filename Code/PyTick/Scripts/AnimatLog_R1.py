# -*- coding:utf-8 -*-
'''
    日志处理模块
    Reference:
    # sphx-glr-gallery-pie-and-polar-charts-nested-pie-py
    [1]nested pie chartshttps://matplotlib.org/3.2.0/gallery/pie_and_polar_charts/nested_pie.html
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
    closeSignal = pyqtSignal()
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
        self.staticPieCanvas = FigureCanvas(
            Figure(figsize=(6, 4), dpi=100, facecolor="none"))
        self.staticPieCanvas.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainlayout.addWidget(self.staticPieCanvas)
        butlayout = QHBoxLayout()
        self.button_1 = QPushButton("Draw")
        self.button_2 = QPushButton("Today")
        self.button_3 = QPushButton("Clf")
        self.button_4 = QPushButton("Pop")
        self.button_1.setStyleSheet(self.pushStyle_1)
        self.button_2.setStyleSheet(self.pushStyle_1)
        self.button_3.setStyleSheet(self.pushStyle_1)
        self.button_4.setStyleSheet(self.pushStyle_1)

        mainlayout.addLayout(butlayout)
        butlayout.addWidget(self.button_1)
        butlayout.addWidget(self.button_2)
        butlayout.addWidget(self.button_3)
        butlayout.addWidget(self.button_4)

        self.setLayout(mainlayout)
        self.setStyleSheet("border:1px solid #eaeaea;border-radius:12px;")

        self.button_1.clicked.connect(self.StaticDrawPie_R2)
        self.button_2.clicked.connect(self.drawToday)
        self.button_3.clicked.connect(self.__clf__)

    def __GenList__(self):
        self.logDetailList = list()
        self.todayDetailList = list()
        try:
            with open(pathm.GetLogFile(), 'r', encoding='utf-8') as f:
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

    # 关闭事件
    def closeEvent(self, event):
        self.closeSignal.emit()


class PopUp(QWidget):
    logDetailList = list()
    todayDetailList = list()
    timer_1 = QTimer()

    def __init__(self):
        super().__init__()
        self.__GenList__()
        self.setupUI()
        # 整体style设置
        self.setStyleSheet(
            "border:1px solid #eaeaea;border-radius:2px;background:transparent;font-size:18px;")
        self.timer_1.timeout.connect(self.showToday)

    def setupUI(self):
        self.setWindowTitle("pop ui")
        mainlayout = QGridLayout()

        # 下拉选项
        self.select = QComboBox(self)
        self.select.addItem("Day")
        self.select.addItem("Mon")
        self.select.addItem("Stop")
        self.select.activated[str].connect(self.itemHandle)

        # 布局
        mainlayout.addWidget(self.select, 0, 0, 1, 1)
        self.matCanvas = FigureCanvas(
            Figure(figsize=(6, 4), dpi=100, facecolor="none"))
        self.matCanvas.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainlayout.addWidget(self.matCanvas, 1, 0, 9, 9)

        self.matCanvas.figure.clf()
        ax = self.matCanvas.figure.subplots()
        # 设置背景图片
        """
        # with cbook.get_sample_data(os.path.join(pathm.GetUiPath(), r"Background-2.jpg")) as image_file:
        #     image = plt.imread(image_file)
        # self.matCanvas.figure.figimage(image)

        """
        # 改变为sinc 初始图形
        x = linspace(0, 3.14*2, num=100)
        y = sinc(x)
        ax.plot(x, y, marker='o', linewidth=2, markersize=3, color='gray')
        xlabes = linspace(0, 25, num=24)
        ax.set_xticklabels(str(xlabes))
        ax.axis('off')  # clear x-axis and y-axis
        self.matCanvas.setStyleSheet("background-color:transparent;")
        self.matCanvas.figure.canvas.draw()
        self.setLayout(mainlayout)

    def __GenList__(self):
        self.logDetailList = list()
        self.todayDetailList = list()
        try:
            with open(pathm.GetLogFile(), mode='r', encoding='utf-8') as f:
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
                    if False:
                        dateToday = datetime.today()
                    else:
                        dateToday = datetime.strptime("2020-04-04", "%Y-%m-%d")
                    today_detail = [dateToday.month, dateToday.day]
                    cowOne_detail = [CowOne.month, CowOne.day]
                    CowTwo_detail = [CowTwo.month, CowTwo.day]
                    if today_detail == cowOne_detail == CowTwo_detail:
                        self.todayDetailList.append(deTemp)
        except:
            self.logDetailList = ['error' for i in range(4)]

    def itemHandle(self):
        if self.select.currentText() == "Day":
            self.startShowToday()
        elif self.select.currentText() == "Stop":
            self.stopShow()
        else:
            pass

    def callout(self):
        print("called me ")
        # if not self.isVisible():
        # self.showMaximized()
        self.show()

    def ReceiveClose(self):
        # 关闭定时器
        if self.timer_1.isActive():
            self.timer_1.stop()
        self.clearCanvas()
        self.close()

    # 设置背景
    def paintEvent(self, event):
        bgpainter = QPainter(self)
        bg = QPixmap(os.path.join(pathm.GetUiPath(), r"Background-2.jpg"))
        bgpainter.drawPixmap(self.rect(), bg)

    def startShowToday(self):
        self.todayDrawIndex = 2
        self.timer_1.start(2000)
        print("start show today")

    def startShowMon(self):
        pass

    def stopShow(self):
        if self.timer_1.isActive():
            self.timer_1.stop()

    def showToday(self):
        if self.todayDrawIndex > len(self.todayDetailList):
            return
        self.matCanvas.figure.clf()
        drawDetail = self.todayDetailList[0:self.todayDrawIndex]
        x = list()
        y = list()
        # idea = list()
        # gap = list()
        for i in drawDetail:
            x_temp = i[0].hour + i[0].minute / 60
            y_temp = int(i[2])
            x.append(x_temp)
            y.append(y_temp)

            x_temp = i[1].hour + i[1].minute / 60
            y_temp = int(i[2])
            x.append(x_temp)
            y.append(y_temp)

        ax = self.matCanvas.figure.subplots()
        # stem([x, ] y, linefmt=None, markerfmt=None, basefmt=None)
        ax.stem(x, y)
        ax.set_xlim(10, 25)
        # ax.set_ylim(0, 120)
        ax.axis('off')
        self.matCanvas.figure.canvas.draw()
        print("way back home")
        self.todayDrawIndex += 1

    def clearCanvas(self):
        self.matCanvas.figure.clf()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if True:
        ex = LogMoudle(pathm.GetLogFile())
        po = PopUp()
        ex.button_4.clicked.connect(po.callout)
        ex.closeSignal.connect(po.ReceiveClose)
        ex.show()
    sys.exit(app.exec_())
    # pyqtgraph.examples.run()
