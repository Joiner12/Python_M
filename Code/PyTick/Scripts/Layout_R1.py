# -*- coding:utf-8-*-
'''
    布局管理
'''

"""
ZetCode PyQt5 tutorial 

In this example, we create a skeleton
of a calculator using a QGridLayout.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

from PyQt5.Qt import QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QMainWindow
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
QGridLayout, QFormLayout, QPushButton, QApplication, QHBoxLayout)
from PyQt5.QtWidgets import QPushButton


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


'''
    1.QMainWindow 和 QWidget的区别 https://blog.csdn.net/superhcq/article/details/53509183
    2.嵌套布局 https://www.cnblogs.com/hhh5460/p/5173645.html
'''


class My_Layout(QWidget):
    def __init__(self):
        super().__init__()
        print('constructor')
        self.initUI()

    def initUI(self):
        print('init main layout')
        mlayout = QHBoxLayout()

        bt1 = QPushButton('1')
        bt2 = QPushButton('2')
        bt3 = QPushButton('3')
        bt4 = QPushButton('4')
        bt5 = QPushButton('5')
        bt6 = QPushButton('6')

        hb = QHBoxLayout()
        vb = QVBoxLayout()
        gb = QGridLayout()

        hbW = QWidget()
        vbW = QWidget()
        gbW = QWidget()

        hb.addWidget(bt1)
        hb.addWidget(bt2)

        vb.addWidget(bt3)
        vb.addWidget(bt4)

        gb.addWidget(bt5)
        gb.addWidget(bt6)


        hbW.setLayout(hb)
        vbW.setLayout(vb)
        gbW.setLayout(gb)


        mlayout.addWidget(hbW)
        mlayout.addWidget(vbW)
        mlayout.addWidget(gbW)

        self.setLayout(mlayout)


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('show text', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", 'You typed:' + textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        """打印完毕之后清空文本框"""
        self.textbox.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exit(app.exec_())

