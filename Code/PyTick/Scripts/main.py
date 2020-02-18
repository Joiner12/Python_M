# -*- coding:utf-8 -*-
from PyTick import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow_1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow_1()
    ui.show()
    sys.exit(app.exec_())
