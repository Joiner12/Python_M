# -*- coding:utf-8-*-
'''
Author:Risky Junior
Data:2020/1/10
'''

import os,sys
import time
from PyQt5.QtCore import pyqtSignal, Qt,QTimer,QTime
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit, QLabel, QRadioButton, QCheckBox,
                             QLineEdit, QGroupBox, QSplitter, QFileDialog)
from PyQt5.QtGui import QIcon, QFont, QTextCursor, QPixmap
from PyQt5.QtGui import QPalette, QBrush, QPixmap


'''
    主级类 (main class)
'''


class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()
        print('PyTick')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
            Icon设置
        '''
        file_path = os.path.abspath(__file__)
        img_src = os.path.abspath(os.path.join(os.path.join(file_path,'../..'),'Src'))
        mainIcon = QIcon(os.path.join(img_src,'Deer.ico'))
        self.setWindowIcon(mainIcon)
        # self.setWindowIcon(QIcon(r'D:\Python_M\Code\PyTick\Scripts\Deer.ico'))
        self.statusBar().showMessage('翻开了我 已经褪了色的相册 再也看不见彩虹的颜色')

        '''
            窗口背景
        '''
        # 使用setStyleSheet 方式实现
        if False:
            self.setObjectName('MainWindow1')
            mainBackGround = os.path.join(img_src,'Background-1.jpg')
            print(mainBackGround)
            self.setStyleSheet("#MainWindow1{border-image:url(Background-1.jpg);}")
            # self.setStyleSheet(r'#MainWindow1{border-image:url(:mainBackGround)};')
        else:
            # 使用palette方式实现
            mainBackGround = os.path.join(img_src,'Background-1.jpg')
            paletteBg = QPalette()
            paletteBg.setBrush(QPalette.Background,QBrush(QPixmap(mainBackGround)))
            self.setPalette(paletteBg)
            # 固定窗口大小
            self.setFixedSize(1024,683)
            self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setGeometry(100, 100, 600, 600*0.618)


        # 更新状态显示时间
        self.timerStatus = QTimer(self)
        self.timerStatus.timeout.connect(self.UpDateStatus)
        self.timerStatus.start(1000)

        # self.resize(1000,683)
        self.setWindowTitle('PyTick')
        self.show()


    #　更新显示信息
    def UpDateStatus(self):
        statusInfo = time.strftime(r'%H:%M:%S',time.localtime(time.time()))
        self.statusBar().showMessage(statusInfo)
        


if __name__ == '__main__':
    os.system('cls')
    if True:
        app = QApplication(sys.argv)
        wm = MainWindow()
        sys.exit(app.exec_())
