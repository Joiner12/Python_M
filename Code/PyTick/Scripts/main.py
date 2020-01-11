# -*- coding:utf-8-*-
'''
Author:Risky Junior
Data:2020/1/10
'''

import os
import sys
from PyQt5.QtCore import pyqtSignal, Qt
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
        print('翻开了我，已经褪了色的相册')


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
        self.statusBar().showMessage('Can\'t see')

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
        self.setGeometry(100, 100, 600, 600*0.618)
        # self.resize(1000,683)
        self.setWindowTitle('翻开')
        self.show()


if __name__ == '__main__':
    os.system('cls')
    if True:
        app = QApplication(sys.argv)
        wm = MainWindow()
        sys.exit(app.exec_())
