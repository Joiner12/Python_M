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
    [11]QListWidget与QTableWidget的使用以及样式设置https://www.cnblogs.com/findumars/p/5655015.html
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
        self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
        self.logpath = r"D:\Codes\Python_M\Code\PyTick\Logs"
        self.setWindowTitle('ITool')
        self.setWindowIcon(QIcon(os.path.join(self.srcpath, r'Deer.ico')))

        mainWidget = QVBoxLayout()

        # QListWidget样式
        self.selectArea = QListWidget()
        self.selectArea.setIconSize(QSize(40, 40))
        self.selectArea.setViewMode(QListView.ListMode)
        self.selectArea.setStyleSheet(self.selectAreaStyle)
        self.selectArea.setSpacing(20)
        self.selectArea.setFixedWidth(180)

        bo = QListWidgetItem('DC')
        self.selectArea.insertItem(0, bo)
        bo.setTextAlignment(Qt.AlignCenter)
        bo.setIcon(QIcon(os.path.join(self.srcpath, r'I-1.ico')))
        bo.setSizeHint(QSize(40, 40))

        ser_1 = QListWidgetItem('AN')
        self.selectArea.insertItem(1, ser_1)
        ser_1.setTextAlignment(Qt.AlignCenter)
        ser_1.setIcon(QIcon(os.path.join(self.srcpath, r'love.png')))
        ser_1.setSizeHint(QSize(40, 40))

        ser_2 = QListWidgetItem('MM')
        ser_2.setTextAlignment(Qt.AlignCenter)
        ser_2.setIcon(QIcon(os.path.join(self.srcpath, r'horse.png')))
        self.selectArea.insertItem(2, ser_2)
        ser_2.setSizeHint(QSize(40, 40))

        ser_3 = QListWidgetItem('MH')
        ser_3.setTextAlignment(Qt.AlignCenter)
        ser_3.setIcon(QIcon(os.path.join(self.srcpath, r'flower.png')))
        self.selectArea.insertItem(3, ser_3)
        ser_3.setSizeHint(QSize(40, 40))
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
        self.setGeometry(200, 200, 600/0.618, 600)

    # 时钟及相应界面
    def stack1UI(self):
        layout = QVBoxLayout()
        self.ticker = ClockStatics_V1()
        sr = '''

        你想要的幸福 其实不在远处
        
        它就是你脚下 一直走的路
        
        '''
        info = QLabel(sr)
        info.setStyleSheet(
            "QLabel{color:#161616;font-size:25px;font-weight:bold;font-family:Consoles;}")
        info.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.ticker)
        layout.addWidget(info)
        self.stack1.setLayout(layout)
        layout.setStretch(0, 4)
        layout.setStretch(1, 6)

    def stack2UI(self):
         # 水平布局
        layout = QHBoxLayout()
        figUI = LogMoudle(r'D:\Codes\Python_M\Code\PyTick\Logs\log2.txt')
        layout.addWidget(figUI)
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

    def paintEvent(self, event):
        bgQp = QPainter(self)
        mainBackGround = os.path.join(self.srcpath, 'Background-2.jpg')
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackWindow()
    demo.show()
    sys.exit(app.exec_())
