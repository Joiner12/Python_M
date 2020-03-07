# -*- coding:utf-8 -*-
'''
    时钟功能区

    ref:
    [1]Qt 之 QLCDNumber https://blog.csdn.net/liang19890820/article/details/50917205
    [2]qLCDnumber https://www.riverbankcomputing.com/static/Docs/PyQt4/qLCDnumber.html
    [3]pyqt实现时钟效果 https://www.pythontab.com/html/2013/pythongui_0703/474.html
    [4]pyqt实现简易时钟 https://blog.csdn.net/Kprogram/article/details/83623079
    [5]PyQt5基本控件详解之QPushButton（六）https://blog.csdn.net/jia666666/article/details/81513443
    [6]计算时间差 https://www.cnblogs.com/SophiaTang/archive/2012/03/25/2417031.html
    [7]python--利用datetime模块计算时间差https://blog.csdn.net/wo1182929447/article/details/77841529?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
    [8]python datetime处理时间 https://www.cnblogs.com/lhj588/archive/2012/04/23/2466653.html
    [9]PyQt5布局管理之QSplitter（六）https://blog.csdn.net/jia666666/article/details/81705675
    [10]PyQt的Layout的比例化分块 https://blog.csdn.net/weixin_33995481/article/details/86275539
    [11]QSplitter分割界面 初始比例https://blog.csdn.net/imxiangzi/article/details/52584599
    [12]setStyleSheet 一些QSS设置的集合https://www.cnblogs.com/xj626852095/p/3648112.html
    [13]QPushButton 按钮设置大小颜色以及字体的大小https://blog.csdn.net/qq_44920726/article/details/102575334
    [14]qss样式表之QPushButton https://blog.csdn.net/aiwangtingyun/article/details/94462976
    [15]QLCDNumber使用https://blog.csdn.net/xuancailinggan/article/details/77487705
    [16]PyQt5系列教程（8）：标准输入对话框https://zhuanlan.zhihu.com/p/29101077
    [17]Python读写文本三种方式 https://zhuanlan.zhihu.com/p/21347291
    [18]Python读写txt文本文件 https://www.cnblogs.com/hackpig/p/8215786.html
    [19]python报错 TypeError: bad operand type for unary +: 'str' 的解决办法
     https://stackoverflow.com/questions/29880136/python-2-7-typeerror-bad-operand-type-for-unary-str
    [20]PyQt信号与槽之多窗口数据传递（七）https://blog.csdn.net/jia666666/article/details/81781697
    [21]打开文件https://blog.csdn.net/humanking7/article/details/80546728
    [22]python运行其他程序方式https://blog.csdn.net/Jerry_1126/article/details/46584179
    [23]判断文件是否存在https://blog.csdn.net/samxx8/article/details/6284960
    [24]os.path https://www.runoob.com/python/python-os-path.html
'''

import sys
import os
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ClockStatics(QWidget):
    def __init__(self):
        super().__init__()
        # 文件路径暂采用绝对路径
        self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
        self.logfile = r'D:\Codes\Python_M\Code\PyTick\Logs\log.txt'
        self.Timing = False
        self.setupUI()
        self.setGeometry(100, 100, 500, 200)

    def setupUI(self):
        WholeLCDLayout = QHBoxLayout()

        self.LCD = QLCDNumber(self)
        self.LCD.setDigitCount(8)
        self.LCD.setMode(QLCDNumber.Dec)
        self.LCD.setSegmentStyle(QLCDNumber.Flat)
        self.LCD.setStyleSheet(
            "QLCDNumber{border:2px solidgreen;color:rgb(102, 212, 209 );}")
        # "QLCDNumber{font-size:100px;}")
        self.LCD.setAutoFillBackground(True)
        self.LCD.setFrameShape(QFrame.StyledPanel)
        self.LCD.setFrameShadow(QFrame.Sunken)
        self.LCD.setSizePolicy(QSizePolicy.Expanding,
                               QSizePolicy.Expanding)
        self.StartTime = datetime.now()
        self.StopTime = datetime.now()
        self.gap = datetime.now()-datetime.now()
        # button area
        ButtonAreaLayout = QVBoxLayout()

        # 按钮样式-1
        self.buttonStyle_1 = ("QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(2, 9, 34);}"
                              "QPushButton{border:2px solid rgb(118,154,40);}"
                              "QPushButton:hover{background:rgb(118,154,40);}")
        # 按钮样式-2 enable = False
        self.buttonStyle_2 = ("QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(2, 9, 34);}"
                              "QPushButton{border:2px solid rgb(118,154,40);}"
                              "QPushButton:hover{background:rgb(118,154,40);}")

        self.StartButton = QPushButton('START')
        self.StartButton.clicked.connect(self.PushLCD)
        self.StartButton.setIcon(
            QIcon(os.path.join(self.srcpath, "启动-2.png")))
        self.StartButton.setStyleSheet(self.buttonStyle_1)

        self.TrackButton = QPushButton('TRACK')
        self.TrackButton.setIcon(
            QIcon(os.path.join(self.srcpath, "记录-1.png")))
        self.TrackButton.setStyleSheet(self.buttonStyle_1)
        self.TrackButton.clicked.connect(self.TrackLCD)

        self.ManualButton = QPushButton("MANUAL")
        self.ManualButton.setIcon(
            QIcon(os.path.join(self.srcpath, "打开-1.png")))
        self.ManualButton.setStyleSheet(self.buttonStyle_2)
        self.ManualButton.clicked.connect(self.ManmalTrack)

        # button area
        ButtonAreaLayout.addWidget(self.StartButton)
        ButtonAreaLayout.addWidget(self.TrackButton)
        ButtonAreaLayout.addWidget(self.ManualButton)

        WholeLCDLayout.addWidget(self.LCD)
        WholeLCDLayout.addLayout(ButtonAreaLayout)

        WholeLCDLayout.setStretch(0, 8)
        WholeLCDLayout.setStretch(1, 2)
        self.BaseTicker = QTimer(self)
        self.BaseTicker.timeout.connect(self.UpdateLCD)
        self.BaseTicker.start(1000)

        self.setLayout(WholeLCDLayout)

    def PushLCD(self):
        # Start 👉 Stop(计时开始)
        if self.StartButton.text() == "START":
            self.StartButton.setText("STOP")
            self.StartButton.setIcon(
                QIcon(os.path.join(self.srcpath, "停止-1.png")))
            self.TrackButton.setEnabled(False)
            self.StartTime = datetime.now()
            self.StopTime = self.StartTime
            self.gap = self.StopTime - self.StartTime
            self.Timing = True
            self.LCD.setStyleSheet(
                "QLCDNumber{border:2px solidgreen;color:rgb(35, 107, 185 );}")
        else:
            # Stop 👉 Star(计时停止)
            self.StartButton.setText("START")
            self.StartButton.setIcon(
                QIcon(os.path.join(self.srcpath, "启动-2.png")))
            self.TrackButton.setEnabled(True)
            self.LCD.setStyleSheet(
                "QLCDNumber{border:2px solidgreen;color:rgb(102, 212, 209 );}")
            self.Timing = False
            # 更新时间
            self.StopTime = datetime.now()
            self.gap = self.StopTime - self.StartTime

    def TrackLCD(self):
        # 有效记录
        if int(self.gap.seconds) >= 0:
            self.gap = datetime.now() - datetime.now()
            self.__Writelog__()
        else:
            pass

    def UpdateLCD(self):
        if self.Timing:
            gap = datetime.now() - self.StartTime
            '''创建时间字符串'''
            time = QTime(gap.seconds/3600, gap.seconds/60, gap.seconds % 60)
            text = time.toString('hh:mm:ss')
            self.LCD.display(text)
        else:
            self.LCD.display(datetime.now().strftime("%H:%M:%S"))

    def ManmalTrack(self):
        # 读取并打开单个文件,所以tuple索引为0。
        openfile_name = QFileDialog.getOpenFileName(
            self, '打开日志', '', 'Text Files (*.txt)')
        if os.path.samefile(openfile_name[0], self.logfile):
            os.system(openfile_name[0])
        else:
            pass

    def __Writelog__(self):
        self.gap = self.StopTime - self.StartTime
        if int(self.gap.seconds) >= 30:
            text, ok = QInputDialog.getText(self, 'Track', 'What Did U DO?')
            if ok & (text.strip() != ""):
                f = open(self.logfile, 'a+', encoding='UTF-8')
                allLines = f.readlines()
                item = datetime.strftime(self.StartTime, "%Y-%m-%d %H:%M:%S") + \
                    "|" + datetime.strftime(self.StopTime, "%Y-%m-%d %H:%M:%S")
                item = item + "|" + str(int(self.gap.seconds/60))+"|"
                item = item + text
                allLines.append(item+"\n")
                f.writelines(allLines)
                f.close()
                # self.gap置零
                self.gap = datetime.now() - datetime.now()
                self.StartTime = datetime.now()
                self.StopTime = datetime.now()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = ClockStatics()
    form.show()
    app.exec_()
