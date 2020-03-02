# -*- coding:utf-8 -*-

from PyQt5.QtCore import *
import sys
import os
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SmokeArea(QWidget):
    def __init__(self):
        self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
        super().__init__()
        self.setStyleSheet(
            "QWidget{border-radius:16px;font-size:22px;font-weight:bold;color:rgb(2, 9, 34);}"
            "QWidget{border:2px solid rgb(195, 227, 81);}"
            "QWidget:hover{background:rgb(195, 227, 81 );}")
        print('smoking area')

    def Update(self):
        pass

    def paintEvent(self, event):
        bgQp = QPainter(self)
        mainBackGround = os.path.join(self.srcpath, 'smoking-2.jpg')
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SmokeArea()
    ex.show()
    sys.exit(app.exec_())
