# -*- coding:utf-8 -*-
'''
    pytick developing
'''

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Clock_R1 import ClockStatics_V1
from ScrollText_R1 import SrollTxt
# from StaticArea_R1 import StaticsArea, StaticsArea_1
from AnimatLog_R1 import LogMoudle
from LrcShine_R1 import SearchBar
import PathManager as pathm


class StackWindow(QWidget):
    selectAreaStyle = (
        "QListWidget{font-size:16px;font-weight:bold;color:rgb(67, 9, 34);}"
        "QListWidget{border:4px;border-radius:4px;}"
        "QListWidget{background-color:transparent;}")

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # 环境配置
        if False:
            self.srcpath = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "Src")
            self.logpath = os.path.join(os.path.dirname(
                os.path.dirname(__file__)), r"Log")
        self.srcpath = pathm.GetUiPath()
        self.logpath = pathm.GetLogPath()
        self.setWindowTitle('ITool')
        self.setWindowIcon(QIcon(os.path.join(self.srcpath, r'Deer.ico')))

        mainWidget = QVBoxLayout()

        # QListWidget样式
        self.selectArea = QListWidget()
        self.selectArea.setIconSize(QSize(40, 30))
        self.selectArea.setViewMode(QListView.ListMode)
        self.selectArea.setStyleSheet(self.selectAreaStyle)
        self.selectArea.setSpacing(20)
        self.selectArea.setFixedWidth(130)

        bo = QListWidgetItem('DC')
        self.selectArea.insertItem(0, bo)
        bo.setTextAlignment(Qt.AlignCenter)
        # bo.setIcon(QIcon(os.path.join(self.srcpath, r'I-1.ico')))
        bo.setSizeHint(QSize(40, 30))

        ser_1 = QListWidgetItem('AN')
        self.selectArea.insertItem(1, ser_1)
        ser_1.setTextAlignment(Qt.AlignCenter)
        # ser_1.setIcon(QIcon(os.path.join(self.srcpath, r'love.png')))
        ser_1.setSizeHint(QSize(40, 30))

        ser_2 = QListWidgetItem('MM')
        ser_2.setTextAlignment(Qt.AlignCenter)
        # ser_2.setIcon(QIcon(os.path.join(self.srcpath, r'horse.png')))
        self.selectArea.insertItem(2, ser_2)
        ser_2.setSizeHint(QSize(40, 30))

        ser_3 = QListWidgetItem('MH')
        ser_3.setTextAlignment(Qt.AlignCenter)
        # ser_3.setIcon(QIcon(os.path.join(self.srcpath, r'flower.png')))
        self.selectArea.insertItem(3, ser_3)
        ser_3.setSizeHint(QSize(40, 30))
        self.stackArea = QStackedWidget(self)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()

        self.stackArea.addWidget(self.stack1)
        self.stackArea.addWidget(self.stack2)
        self.stackArea.addWidget(self.stack3)
        self.stackArea.addWidget(self.stack4)

        mainHLayout = QSplitter(Qt.Horizontal)
        mainHLayout.setHandleWidth(1)

        mainHLayout.addWidget(self.selectArea)
        mainHLayout.addWidget(self.stackArea)

        mainHLayout.setStretchFactor(0, 8)
        mainHLayout.setStretchFactor(1, 2)

        # information bar area
        self.infoBar = SrollTxt()
        self.infoBar.setFixedHeight(20)

        mainWidget.addWidget(mainHLayout)
        mainWidget.addWidget(self.infoBar)

        mainWidget.setStretch(0, 9)
        mainWidget.setStretch(1, 1)
        # 绑定stack
        self.selectArea.currentRowChanged.connect(self.display)
        self.setLayout(mainWidget)
        self.setFixedSize(400/0.618, 400)
        self.move(200, 200)

    # 时钟及相应界面
    def stack1UI(self):
        layout = QVBoxLayout()
        self.ticker = ClockStatics_V1()
        sr = """<p style="color:#161616;font-size:22px;font-weight:bold;">
        The happiness you seek,in fact<br>
        is not far away. <br>
        It is the road you have been walking.
        </p>"""
        info = QLabel(sr)
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.ticker)
        layout.addWidget(info)
        self.stack1.setLayout(layout)
        layout.setStretch(0, 4)
        layout.setStretch(1, 6)

    def stack2UI(self):
         # 水平布局
        layout = QHBoxLayout()
        figUI = LogMoudle(os.path.join(pathm.GetLogPath(), r"log.txt"))
        layout.addWidget(figUI)
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QVBoxLayout()
        self.lrcwarpper = SearchBar()
        layout.addWidget(self.lrcwarpper)
        self.stack3.setLayout(layout)

    def stack4UI(self):
        layout = QVBoxLayout()
        # self.Static = StaticsArea()
        # layout.addWidget(self.Static)
        self.stack4.setLayout(layout)

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stackArea.setCurrentIndex(i)

    def paintEvent(self, event):
        bgQp = QPainter(self)
        mainBackGround = os.path.join(self.srcpath, 'Background-5.jpg')
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackWindow()
    demo.show()
    sys.exit(app.exec_())
