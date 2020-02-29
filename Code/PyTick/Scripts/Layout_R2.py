# -*- encoding:utf-8 -*-
'''

    Ref:
    [1] QListWidget 设置样式 https://www.bbsmax.com/A/KE5QOlL0zL/
    [2] 设置QListWidget透明背景 https://blog.csdn.net/liyan728/article/details/8955634
    [3] QSplitter 分割线 https://blog.csdn.net/skykingf/article/details/8247593
    [4] QListWidgetItem带上颜色的问题 https://www.cnblogs.com/hushaojun/p/4632843.html
    [5] QT控制选中item的文字颜色(HighlightedText) 和 QT表格交替背景色 
    https://blog.csdn.net/aisq2008/article/details/6393874?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
'''
import sys
import os
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QMainWindow)

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class StackWindow(QWidget):
    def __init__(self):
        print('constructor')
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
        print('setup ui')
        self.setWindowTitle('翻开了我已经褪了色的相册')
        self.setWindowIcon(QIcon(os.path.join(self.srcpath, r'Deer.ico')))

        # 主窗垂直布局(3/3) +  分割
        mainWidget = QHBoxLayout()

        # QListWidget样式
        self.selectArea = QListWidget()
        self.selectArea.setIconSize(QSize(50, 50*0.618))
        self.selectArea.setViewMode(QListView.ListMode)
        selectAreaStyle = "border: 1px; background-color: transparent"
        self.selectArea.setStyleSheet(selectAreaStyle)

        bo = QListWidgetItem('我')
        self.selectArea.insertItem(0, bo)
        bo.setTextAlignment(Qt.AlignCenter)
        bo.setIcon(QIcon(os.path.join(self.srcpath, r'I-1.ico')))
        bo.setSizeHint(QSize(60, 60))

        ser_1 = QListWidgetItem('爱你')
        self.selectArea.insertItem(1, ser_1)
        ser_1.setTextAlignment(Qt.AlignCenter)
        ser_1.setIcon(QIcon(os.path.join(self.srcpath, r'love.png')))
        ser_1.setSizeHint(QSize(60, 60))

        ser_2 = QListWidgetItem('MM')
        ser_2.setTextAlignment(Qt.AlignCenter)
        ser_2.setIcon(QIcon(os.path.join(self.srcpath, r'horse.png')))
        self.selectArea.insertItem(2, ser_2)
        ser_2.setSizeHint(QSize(60, 60))

        ser_3 = QListWidgetItem('麻花儿')
        ser_3.setTextAlignment(Qt.AlignCenter)
        ser_3.setIcon(QIcon(os.path.join(self.srcpath, r'flower.png')))
        self.selectArea.insertItem(3, ser_3)
        ser_3.setSizeHint(QSize(60, 60))
        self.stackArea = QStackedWidget(self)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.stackArea.addWidget(self.stack1)
        self.stackArea.addWidget(self.stack2)
        self.stackArea.addWidget(self.stack3)

        mainlayout = QSplitter(Qt.Horizontal)
        mainlayout.setHandleWidth(1)

        mainlayout.addWidget(self.selectArea)
        mainlayout.addWidget(self.stackArea)

        mainlayout.setStretchFactor(0, 9)
        mainlayout.setStretchFactor(1, 1)
        self.selectArea.setFixedWidth(150)

        mainWidget.addWidget(mainlayout)

        # 绑定stack
        self.selectArea.currentRowChanged.connect(self.display)
        self.setLayout(mainWidget)
        self.setGeometry(200, 200, 600/0.618, 600)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名', QLineEdit())
        layout.addRow('地址', QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        # 主表单布局，次水平布局
        if False:
            layout = QFormLayout()
            sex = QHBoxLayout()

            # 水平布局添加单选按钮
            sex.addWidget(QRadioButton('男'))
            sex.addWidget(QRadioButton('女'))

            # 表单布局添加控件
            layout.addRow(QLabel('性别'), sex)
            layout.addRow('生日', QLineEdit())
            self.stack2.setLayout(layout)
        else:
            layout = QHBoxLayout()
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
            layout.addWidget(info)

            self.stack2.setLayout(layout)

    def stack3UI(self):
        # 水平布局
        layout = QHBoxLayout()

        # 添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stackArea.setCurrentIndex(i)

    def paintEvent(self, event):
        bgQp = QPainter(self)
        file_path = os.path.abspath(__file__)
        img_src = os.path.abspath(os.path.join(
            os.path.join(file_path, '../..'), 'Src'))
        mainBackGround = os.path.join(img_src, 'bg-2.jpg')
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackWindow()
    demo.show()
    sys.exit(app.exec_())
