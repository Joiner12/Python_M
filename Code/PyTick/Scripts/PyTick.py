# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_PyTick import Ui_MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    ma = QMainWindow()
    win.setupUi(ma)
    ma.show()
    sys.exit(app.exec_())
    print('ui')
