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

from datetime import datetime
from numpy import random, arange
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
    srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
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
        self.__GenList__()
        fileflag = os.path.exists(logpath)
        self.setupUI()
        self.__showImg__()
        self.time_01 = QTimer()

    def setupUI(self):
        mainlayout = QVBoxLayout()
        self.staticPieCanvas = FigureCanvas(Figure(figsize=(6, 4), dpi=100))
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

        self.button_1.clicked.connect(self.StaticDrawPie)
        self.button_2.clicked.connect(self.drawToday)
        self.button_3.clicked.connect(self.__clf__)

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
                    # today
                    dateToday = datetime.today()
                    if dateToday.day == CowOne.day and dateToday.day == CowTwo.day:
                        self.todayDetailList.append(deTemp)
        except:
            self.logDetailList = ['error' for i in range(4)]

    def StaticDrawPie(self):
        self.staticPieCanvas.figure.clf()
        self.sPieDraw = self.staticPieCanvas.figure.subplots()
        if len(self.logDetailList) > 1 and False:
            dayGap = list()
            labels = list()
            for i in self.logDetailList:
                dayGap.append(i[2])
                labels.append(i[3])
            dayGap = random.randint(1, 10, size=10)
            labels = labels[0:10]
            self.sPieDraw.pie(dayGap, labels=labels, radius=1, wedgeprops=dict(
                width=0.4, edgecolor='w'))
            self.sPieDraw.pie(dayGap, counterclock=False, radius=1-0.3, wedgeprops=dict(
                width=0.3, edgecolor='w'))
        else:
            if len(self.todayDetailList) > 0:
                things = list()
                duration = list()
                whenDo = list()
                for i in self.todayDetailList:
                    things.append(i[3])
                    duration.append(int(i[2]))
                    whenDo.append(i[0].strftime("%H:%M") +
                                  i[1].strftime("%H:%M"))

                self.sPieDraw.pie(duration, labels=things, radius=1, wedgeprops=dict(
                    width=0.4, edgecolor='w'))
                self.sPieDraw.pie(duration, counterclock=False, radius=1-0.3, wedgeprops=dict(
                    width=0.3, edgecolor='w'))
        self.staticPieCanvas.figure.canvas.draw()

    def DynamicDrawPie(self):
        pass

    def drawToday(self):
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
            self.staticPieCanvas.figure.canvas.draw()
        else:
            self.__showImg__()

    def __clf__(self):
        self.staticPieCanvas.figure.clf()
        self.staticPieCanvas.figure.canvas.draw()

       # show image
    def __showImg__(self):
        self.staticPieCanvas.figure.clf()
        ax = self.staticPieCanvas.figure.subplots()
        with cbook.get_sample_data(os.path.join(self.srcpath, 'horse.png')) as image_file:
            image = plt.imread(image_file)
        ax.imshow(image)
        ax.axis('off')  # clear x-axis and y-axis
        self.staticPieCanvas.figure.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if True:
        ex = LogMoudle(r'D:\Codes\Python_M\Code\PyTick\Logs\log.txt')
        ex.show()
    sys.exit(app.exec_())
    # pyqtgraph.examples.run()
