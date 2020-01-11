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
        self.statusBar().showMessage('已经被我泪水淹没...')
        self.setGeometry(100, 100, 600, 600*0.618)
        self.setWindowIcon(QIcon(r"..//Src//Watchclock.png"))
        self.setWindowTitle('翻开')
        self.show()


if __name__ == '__main__':
    os.system('cls')
    app = QApplication(sys.argv)
    wm = MainWindow()
    sys.exit(app.exec_())
