# -*- coding:utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class stackWindow(QWidget):
    def __init__(self):
        super().__init__()
        print('终于你开口向我诉说他有多温柔')

    def setupUI(self):
        print('ui')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wm = stackWindow()
    wm.show()
    sys.exit(app.exec_())
