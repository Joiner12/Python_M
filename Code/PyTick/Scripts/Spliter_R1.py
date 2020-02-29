# -*- coding:utf-8 -*-


import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import Qt
from PyQt5.Qt import *


class Example_spliter(QWidget):
    def __init__(self):
        super(Example_spliter, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter demo')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example_spliter()
    sys.exit(app.exec_())
