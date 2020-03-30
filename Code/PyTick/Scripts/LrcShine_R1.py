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
import random
import re
import PathManager as pathm
srcpath = pathm.GetUiPath()
lrcSrcPath = pathm.GetLrcPath()


class LrcWidget(QWidget):
    lrcSrcPath = lrcSrcPath
    srcpath = srcpath

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pass


class SearchBar(QWidget):
    pushStyle_1 = ("QPushButton{background: transparent;}"
                   "QPushButton:hover{rgb(118,154,40);}")
    editStyle_1 = (
        "QLineEdit{font-size:16px;color:rgb(2, 9, 34);}"
        "QLineEdit{font-weight:bold;}")

    labelStyle_1 = ("QLabel{background:transparent}")

    indexTableLrc = list()

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.CreateIndexTable(lrcSrcPath)

    def setupUI(self):
        # main window layout
        mainLayout = QVBoxLayout()
        # search tab layout
        searchLayout = QHBoxLayout()
        self.searchPushBtn = QPushButton()
        self.editLine = QLineEdit()

        # basic widget & layout
        self.showArea = QLabel()
        searchLayout.addWidget(self.editLine, 10)
        searchLayout.addWidget(self.searchPushBtn, 1)

        mainLayout.addWidget(self.showArea)
        mainLayout.addLayout(searchLayout)
        mainLayout.setStretch(0, 2)
        mainLayout.setStretch(1, 6)

        self.setLayout(mainLayout)

        # widgets function
        self.editLine.returnPressed.connect(self.enterPress)
        self.searchPushBtn.clicked.connect(self.resetButton)

        # style set
        self.searchPushBtn.setStyleSheet(self.pushStyle_1)
        self.setToolTip(r"Search")
        self.searchPushBtn.setIcon(
            QIcon(os.path.join(srcpath, r"search-1.png")))
        self.editLine.setPlaceholderText("黎明的那道光会越过黑暗")
        self.editLine.setStyleSheet(self.editStyle_1)
        # show area style
        self.showArea.setStyleSheet(self.labelStyle_1)
        self.showArea.setAutoFillBackground(True)
        initText = '''< h2 style="color:#ff063c" > SyntaxError EOL While Scanning String Literal < /h2 >''' \
            '''<p style="color:#ff063c;font-size:16px;font-weight:bold">
            SyntaxError are detected before the programs runs.</p>'''
        self.showArea.setText(initText)
        self.showArea.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(
            "height:29px;border:1px solid #eaeaea;border-radius:12px;")
        self.setGeometry(20, 50, 400, 300)

    def enterPress(self):
        # self.__SearchLrc__()
        getStr = list()
        tempstr = self.editLine.text()
        for i in range(int(len(tempstr)/20)):
            getStr.append(tempstr[i*20:int((i+1)*20-1)])
        getStr.append(tempstr[-1*int(len(tempstr) % 20)-1:])

        showtext = ""
        for j in getStr:
            showtext += '''<p style = "color:#7a8588;font-size:16PX;" >''' + j + ''' </p >'''
        self.__updateLabel__(showtext)

    def resetButton(self):
        你的答案 = '''
            <h1 style = "color:#7a8588;" >
            你的答案
            </h1 >
            <p style = "color:#7a8588;font-size:12PX;" >
            也许世界就这样 我也还在路上
            </p >
            <p style = "color:#7a8588;font-size:12PX;" >
            没有人能诉说 也许我只能沉默
            </p >
            <p style = "color:#ff0000;font-size:16px;font-weight:bold;" >
            眼泪湿润眼眶 可又不甘懦弱
            </p >
            <p style = "color:#7a8588;font-size:12PX;" >
            低着头 期待白昼 接受所有的嘲讽
            </p >
            <p style = "color:#7a8588;font-size:12PX;" >
            接受所有的嘲讽
            </p >
            <p style = "color:#7a8588;font-size:12PX;" >
            迎着风 拥抱彩虹
            </p >
            <p style = "color:#7a8588;font-size:12PX;" >
            勇敢的向前走
            </p >
            '''

        self.__updateLabel__(你的答案)

    # get the similarity of string

    def __SearchLrc__(self):
        posLrc = 0
        piece = self.editLine.text()
        if len(self.indexTableLrc) < 10 or len(piece.strip("")) == 0:
            return ""
        else:
            nameTable = [i[1] for i in self.indexTableLrc]
            if piece in nameTable:
                posLrc = nameTable.index(piece)

    # create index table
    def CreateIndexTable(self, src_path):
        if not os.path.exists(src_path):
            self.indexTableLrc = list()
        else:
            fileTemp = os.walk(src_path)
            # walk = (当前文件夹,子文件夹,子文件)
            with open(os.path.join(src_path, r'IndexLrc.txt'), encoding='utf-8', mode='w') as indexOut:
                cnt = 0
                for i in fileTemp:
                    cnt += 1
                    if cnt > 0:
                        for j in i[2]:
                            detail_temp = list()
                            info_temp = os.path.join(i[0], j)
                            file_temp = os.path.join("", j)
                            detail_temp.append(i[0])
                            detail_temp.append(file_temp)
                            indexOut.writelines('%s\n' % (info_temp))
                            self.indexTableLrc.append(detail_temp)
                indexOut.close()

    def __updateLabel__(self, detail):
        self.showArea.setText(detail)

    # mouse event
    # def leaveEvent(self, event):
    def mouseDoubleClickEvent(self, event):
        up_limit = len(self.indexTableLrc)
        curIndex = random.randint(1, up_limit)
        piece = self.indexTableLrc[curIndex]
        name = piece[1]
        name = name.strip(".lrc")
        words = list()
        detail = list()
        with open(os.path.join(piece[0], piece[1]), encoding='utf-8', mode='r') as f:
            detail = f.readlines()
            if not f.closed:
                f.close()
        if len(detail) > 10:
            randindex = random.randint(5, len(detail) - 3)
            temp_1 = detail[randindex:randindex + 2]
            for i in temp_1:
                piece_pattern = re.compile(r"\[.+\]")
                i_temp = piece_pattern.sub(" ", i)
                i_temp = i_temp.strip()
                words.append(i_temp)
            if len(name) > 15 or len(words[0]) > 25 or len(words[1]) > 25:
                return
            # error length string check
            name = "<h1 style='color:#1d8388'>" + name + "</h1>"
            word_1 = '''<p style="color:#ff007f;font-size:16px;font-weight:bold">''' + \
                words[0]+'''</p>'''
            word_2 = '''<p style="color:#ff007f;font-size:16px;font-weight:bold">''' + \
                words[1]+'''</p>'''

            final = name + "<br>" + word_1 + word_2
            self.__updateLabel__(final)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchBar()
    ex.show()
    sys.exit(app.exec_())
