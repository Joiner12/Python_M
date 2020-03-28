# -*- coding:utf-8 -*-
"""
    Lrc Shine

    1.Chrome https://blog.csdn.net/u010155023/article/details/50731034
    2.调用https://blog.csdn.net/winycg/article/details/78512300
"""
import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
lrcSrcPath = r"D:\Codes\Python_M\Src\LRC"


class LrcWidget(QWidget):
    lrcSrcPath = r"D:\Codes\Python_M\Code\PyTick\Src"
    srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"

    def __init__(self):
        super().__init__()
        print("lrc constructor")
        self.setupUI()

    def setupUI(self):
        pass


class SearchBar(QWidget):
    pushStyle_1 = ("QPushButton{background: transparent;}"
                   "QPushButton:hover{rgb(118,154,40);}")
    editStyle_1 = (
        "QLineEdit{font-size:16px;color:rgb(2, 9, 34);}"
        "QLineEdit{font-weight:bold;}")
    indexTableLrc = list()

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.CreateIndexTable(lrcSrcPath)
        self.show()

    def setupUI(self):
        # main window layout
        mainLayout = QHBoxLayout()
        self.searchPushBtn = QPushButton()
        self.editLine = QLineEdit()

        # basic widget & layout
        mainLayout.addWidget(self.editLine, 10)
        mainLayout.addWidget(self.searchPushBtn, 1)
        self.setLayout(mainLayout)

        # widgets function
        self.editLine.returnPressed.connect(self.enterPress)
        self.searchPushBtn.clicked.connect(self.enterPress)

        # style set
        self.searchPushBtn.setStyleSheet(self.pushStyle_1)
        self.setToolTip(r"Search")
        self.searchPushBtn.setIcon(
            QIcon(os.path.join(srcpath, r"search-1.png")))
        self.editLine.setPlaceholderText("黎明的那道光会越过黑暗")
        self.editLine.setStyleSheet(self.editStyle_1)
        self.setStyleSheet(
            "height:29px;border:1px solid #eaeaea;border-radius:12px;")
        self.setGeometry(20, 50, 200, 20)

    def enterPress(self):
        print(self.editLine.text())

    # get the similarity of string
    def __SearchLrc__(self):
        if not os.path.exists(os.path.join(src_path, r'IndexLrc.txt')):
            return ""

    # create index table

    def CreateIndexTable(self, src_path):
        if not os.path.exists(src_path):
            self.indexTableLrc = list()
        else:
            fileTemp = os.walk(src_path)
            with open(os.path.join(src_path, r'IndexLrc.txt'), encoding='utf-8', mode='w') as indexOut:
                cnt = 0
                for i in fileTemp:
                    cnt += 1
                    if cnt > 0:
                        for j in i[2]:
                            info_temp = os.path.join(i[0], j)
                            print(info_temp, j)
                            indexOut.writelines('%s\n' % (info_temp))
                        print(cnt)
                indexOut.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchBar()
    sys.exit(app.exec_())
