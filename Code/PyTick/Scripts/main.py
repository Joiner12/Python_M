# -*- coding:utf-8-*-
'''
Author:Risky Junior
Data:2020/1/10
'''

import os
import sys
import time
from PyQt5.QtCore import pyqtSignal, Qt, QTimer, QTime
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit, QLabel, QRadioButton, QCheckBox,
                             QLineEdit, QGroupBox, QSplitter, QFileDialog)
from PyQt5.QtGui import QIcon, QFont, QTextCursor
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter


'''
    主级类 (main class)
'''


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
            Icon设置
        '''
        file_path = os.path.abspath(__file__)
        img_src = os.path.abspath(os.path.join(
            os.path.join(file_path, '../..'), 'Src'))
        mainIcon = QIcon(os.path.join(img_src, 'Deer.ico'))
        self.setWindowIcon(mainIcon)
        # self.setWindowIcon(QIcon(r'D:\Python_M\Code\PyTick\Scripts\Deer.ico'))
        self.statusBar().showMessage('翻开了我 已经褪了色的相册 再也看不见彩虹的颜色')
        '''
            按钮
        '''
        okButton = QPushButton('CLOCK', self)
        self.b1 = okButton
        okButton.setIcon(
            QIcon(QPixmap(r'D:\Codes\Python_M\Code\PyTick\Src\Deer.ico')))
        okButton.setCheckable(True)
        okButton.setGeometry(100, 100, 80, 70*0.62)
        okButton.clicked[bool].connect(self.Jump_1)

        '''
        窗口布局的方式不需要使用盒子 格栅的方式 通过调整坐标的方式手动完成
        '''

        # 固定窗口大小
        self.setFixedSize(1024, 683)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)

        # menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        '''
            状态显示时间信息定时器
        '''
        # 更新状态显示时间
        self.timerStatus = QTimer(self)
        self.timerStatus.timeout.connect(self.UpDateStatus)
        self.timerStatus.start(1000)

        '''
            Label
        '''
        # lab_1 = QLabel('Label_1',self)
        # lab_1.move(120,120)

        '''
            主窗显示
        '''
        # self.resize(1000,683)
        self.setGeometry(200, 200, 600, 600*0.618)
        self.setWindowTitle('PyTick')

        self.show()

    #　状态显示信息修改为系统时间

    def UpDateStatus(self):
        statusInfo = time.strftime(r'%H:%M:%S', time.localtime(time.time()))
        self.statusBar().showMessage(statusInfo)

    '''
        重写paintEvent实现背景修改
    '''

    def paintEvent(self, event):
        bgQp = QPainter(self)
        file_path = os.path.abspath(__file__)
        img_src = os.path.abspath(os.path.join(
            os.path.join(file_path, '../..'), 'Src'))
        mainBackGround = os.path.join(img_src, 'Deer-3.png')
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)

    def Jump_1(self, pressed):
        if self.b1.isChecked():
            print('责怪都舍不得')
        else:
            print('xinan')


if __name__ == '__main__':
    os.system('cls')
    if True:
        app = QApplication(sys.argv)
        wm = MainWindow()
        sys.exit(app.exec_())
