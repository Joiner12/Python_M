# -*- coding:utf-8 -*-
'''
    Ref:
    [1] QListWidget 设置样式 https://www.bbsmax.com/A/KE5QOlL0zL/
    [2] 设置QListWidget透明背景 https://blog.csdn.net/liyan728/article/details/8955634
    [3] QSplitter 分割线 https://blog.csdn.net/skykingf/article/details/8247593
    [4] QListWidgetItem带上颜色的问题 https://www.cnblogs.com/hushaojun/p/4632843.html
    [5] QT控制选中item的文字颜色(HighlightedText) 和 QT表格交替背景色
    https://blog.csdn.net/aisq2008/article/details/6393874?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
    [6] PyQt - QLabel Widget https://www.tutorialspoint.com/pyqt/pyqt_qlabel_widget.htm
    [7] PyQt中QLabel背景与字体的一些设置 https://blog.csdn.net/jiuzuidongpo/article/details/45485127
    [8] QPalette https://doc.qt.io/qtforpython/PySide2/QtGui/QPalette.html
    [9] 无边框 https://www.cnblogs.com/jyroy/p/9461317.html
    [10]Layerout https://www.learnpyqt.com/courses/start/layouts/
'''

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Clock_R1 import ClockStatics
from SmokeArea_R1 import SmokeArea
from ScrollText_R1 import SrollTxt


class StackWindow(QWidget):
    def __init__(self):
        print('constructor')
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # 环境配置
        if False:
            self.srcpath = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "Src")
            self.logpath = os.path.join(os.path.dirname(
                os.path.dirname(__file__)), r"Log")
        self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
        self.logpath = r"D:\Codes\Python_M\Code\PyTick\Logs"
        self.setWindowTitle('ITool')
        self.setWindowIcon(QIcon(os.path.join(self.srcpath, r'Deer.ico')))
        # self.setWindowOpacity(0.9)  # 边框透明
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置透明背景
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # 主窗垂直布局(3/3) +  分割
        mainWidget = QVBoxLayout()

        # QListWidget样式
        self.selectArea = QListWidget()
        self.selectArea.setIconSize(QSize(30, 40))
        self.selectArea.setViewMode(QListView.ListMode)
        selectAreaStyle = "border: 1px; background-color: transparent"
        self.selectArea.setStyleSheet(selectAreaStyle)
        self.selectArea.Font = QFont()
        self.selectArea.Font.setPointSize(10)
        self.selectArea.Font.setWeight(60)
        self.selectArea.setFont(self.selectArea.Font)

        bo = QListWidgetItem('Daily Count')
        self.selectArea.insertItem(0, bo)
        bo.setTextAlignment(Qt.AlignCenter)
        bo.setIcon(QIcon(os.path.join(self.srcpath, r'I-1.ico')))
        bo.setSizeHint(QSize(30, 30))

        ser_1 = QListWidgetItem('爱你')
        self.selectArea.insertItem(1, ser_1)
        ser_1.setTextAlignment(Qt.AlignCenter)
        ser_1.setIcon(QIcon(os.path.join(self.srcpath, r'love.png')))
        ser_1.setSizeHint(QSize(30, 30))

        ser_2 = QListWidgetItem('MM')
        ser_2.setTextAlignment(Qt.AlignCenter)
        ser_2.setIcon(QIcon(os.path.join(self.srcpath, r'horse.png')))
        self.selectArea.insertItem(2, ser_2)
        ser_2.setSizeHint(QSize(30, 30))

        ser_3 = QListWidgetItem('麻花儿')
        ser_3.setTextAlignment(Qt.AlignCenter)
        ser_3.setIcon(QIcon(os.path.join(self.srcpath, r'flower.png')))
        self.selectArea.insertItem(3, ser_3)
        ser_3.setSizeHint(QSize(30, 30))
        self.stackArea = QStackedWidget(self)
        self.selectArea.setFixedWidth(150)

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
        self.setGeometry(200, 200, 400/0.618, 400)

    # 时钟及相应界面
    def stack1UI(self):
        layout = QVBoxLayout()
        self.ticker = ClockStatics()
        sr = '''
        Stars shining bright above you
        星儿在你头顶闪耀
        Night breezes seem to whisper "I love you"
        夜晚的微风似乎轻轻地在说 我爱你
        Birds singing in the sycamore tree
        鸟儿在梧桐树里歌唱着
        Dream a little dream of me
        愿你的梦里有我
        Say "Night-ie night" and kiss me
        说晚安吧，然后亲吻我
            '''
        info = QLabel(sr)
        info.setStyleSheet(
            "QLabel{color:rgb(216,245,255,250);font-size:15px;font-family:Consoles;}")
        info.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.ticker)
        layout.addWidget(info)
        self.stack1.setLayout(layout)
        layout.setStretch(0, 5)
        layout.setStretch(1, 5)

    def stack2UI(self):
         # 水平布局
        layout = QHBoxLayout()
        # figUI = StaticsArea_1()
        # layout.addWidget(figUI)
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        # 添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.stack3.setLayout(layout)

    def stack4UI(self):
        layout = QVBoxLayout()
        # self.Static = StaticsArea()
        # layout.addWidget(self.Static)
        self.stack4.setLayout(layout)

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stackArea.setCurrentIndex(i)

    # def paintEvent(self, event):
    #     bgQp = QPainter(self)
    #     mainBackGround = os.path.join(self.srcpath, 'bg-2.jpg')
    #     bg = QPixmap(mainBackGround)
    #     bgQp.drawPixmap(self.rect(), bg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackWindow()
    demo.show()
    sys.exit(app.exec_())
