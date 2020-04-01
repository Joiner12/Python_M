# -*- coding:utf-8 -*-
"""
    widget every piece
"""
import PathManager as PathM
from datetime import datetime
import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

'''
    words show area
'''


class FeelWidgetOut(QWidget):
    srcpath = PathM.GetUiPath()
    piecepath = PathM.GetPieceFile()
    QlabelStyle = ("QLabel{background:transparent}")
    wordsList = list()

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # QLABEL AREA
        self.showArea = QLabel()
        self.showArea.setStyleSheet(self.QlabelStyle)

    def updatePiece(self):
        pass

    # 获取文件列表，需要多次调用
    def __genList__(self):
        self.wordsList = list()
        try:
            with open(PathM.GetPieceFile(), mode="r", encoding='utf-8') as f:
                temp = f.readlines()
                if len(temp) > 0:
                    for i in temp:
                        self.wordsList.append(i.strip(""))
                if not f.closed:
                    f.close()
        except:
            self.wordsList.append("Is there many questions in your brain??")


'''
    输入words
'''


class FeelWidgetIn(QWidget):
    editStyle_1 = (
        "QLineEdit{font-size:12px;color:rgb(2, 9, 34);}"
        "QLineEdit{font-weight:bold;}")

    labelStyle_1 = ("QLabel{background:transparent}")

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # search tab layout
        self.editLine = QLineEdit()

        # widgets function
        self.editLine.returnPressed.connect(self.enterPress)
        # style set
        self.editLine.setPlaceholderText("Hey Judy,don't be afraid")
        self.editLine.setStyleSheet(self.editStyle_1)
        # parent layout style sheet
        self.setStyleSheet(
            "height:29px;border:1px solid #eaeaea;border-radius:12px;")
        self.setGeometry(20, 50, 400, 300)

    def enterPress(self):
        tempstr = self.editLine.text()
        try:
            with open(PathM.GetPieceFile(), mode="a+", encoding='utf-8') as f:
                temp = f.readlines()
                if tempstr.replace(" ", "") != temp[-1].replace(" ", "")
                temp.append(tempstr)
        except:
            pass

    # mouse event
    # def leaveEvent(self, event):
    def mouseDoubleClickEvent(self, event):
        pass
