# -*- coding:utf-8 -*-
'''
    时钟功能区
'''

import sys
import os
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MultiInputDialog_R1 import MultiInputDialog


class ClockStatics_V1(QWidget):
    def __init__(self):
        super().__init__()
        # 环境配置
        if False:
            self.srcpath = os.path.join(os.path.dirname(
                os.path.dirname(__file__)), r"Src")
            self.logpath = os.path.join(os.path.dirname(
                os.path.dirname(__file__)), r"Log")
        self.srcpath = r"D:\Codes\Python_M\Code\PyTick\Src"
        self.logpath = r"D:\Codes\Python_M\Code\PyTick\Logs"
        self.Timing = False
        self.setupUI()
        # self.setFixedSize(500, 200)

    def setupUI(self):
        WholeLCDLayout = QHBoxLayout()

        self.LCD = QLCDNumber(self)
        self.LCD.setDigitCount(8)
        self.LCD.setMode(QLCDNumber.Dec)
        self.LCD.setSegmentStyle(QLCDNumber.Flat)
        self.LCD.setStyleSheet(
            "QLCDNumber{border:2px solidgreen;color:rgb(102, 212, 209 );}"
            "QLCDNumber{font-size:100px;}")
        self.LCD.setAutoFillBackground(True)
        self.LCD.setFrameShape(QFrame.StyledPanel)
        self.LCD.setFrameShadow(QFrame.Sunken)
        self.LCD.setSizePolicy(QSizePolicy.Expanding,
                               QSizePolicy.Expanding)
        self.StartTime = datetime.now()
        self.StopTime = datetime.now()
        self.gap = datetime.now()-datetime.now()
        # button area
        ButtonAreaLayout = QVBoxLayout()

        # 按钮样式-1
        self.buttonStyle_1 = ("QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(2, 9, 34);}"
                              "QPushButton{border:2px solid rgb(118,154,40);}"
                              "QPushButton:hover{background:rgb(118,154,40);}")
        # 按钮样式-2 enable = False
        self.buttonStyle_2 = ("QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:#ff5500;}"
                              "QPushButton{border:2px solid rgb(118,154,40);}"
                              "QPushButton:hover{background:rgb(118,154,40);}")

        self.StartButton = QPushButton('START')
        self.StartButton.clicked.connect(self.PushLCD)
        self.StartButton.setIcon(
            QIcon(os.path.join(self.srcpath, "启动-2.png")))
        self.StartButton.setStyleSheet(self.buttonStyle_1)

        self.TrackButton = QPushButton('TRACK')
        self.TrackButton.setIcon(
            QIcon(os.path.join(self.srcpath, "记录-1.png")))
        self.TrackButton.setStyleSheet(self.buttonStyle_1)
        self.TrackButton.clicked.connect(self.TrackLCD)

        self.ManualButton = QPushButton("LOGFL")
        self.ManualButton.setIcon(
            QIcon(os.path.join(self.srcpath, "打开-1.png")))
        self.ManualButton.setStyleSheet(self.buttonStyle_1)
        self.ManualButton.clicked.connect(self.ManmalTrack)

        self.PieceButton = QPushButton("PIECE")
        self.PieceButton.setIcon(
            QIcon(os.path.join(self.srcpath, "文件-1.png")))
        self.PieceButton.setStyleSheet(self.buttonStyle_1)
        self.PieceButton.clicked.connect(self.AddPiece)

        # button area
        ButtonAreaLayout.addWidget(self.StartButton, 1)
        ButtonAreaLayout.addWidget(self.TrackButton, 1)
        ButtonAreaLayout.addWidget(self.PieceButton, 1)
        ButtonAreaLayout.addWidget(self.ManualButton, 1)

        WholeLCDLayout.addWidget(self.LCD)
        WholeLCDLayout.addLayout(ButtonAreaLayout)

        WholeLCDLayout.setStretch(1, 1)
        WholeLCDLayout.setStretch(0, 9)
        self.BaseTicker = QTimer(self)
        self.BaseTicker.timeout.connect(self.UpdateLCD)
        self.BaseTicker.start(1000)

        self.setLayout(WholeLCDLayout)
        self.setMinimumWidth(500)

    def PushLCD(self):
        # Start 👉 Stop(计时开始)
        if self.StartButton.text() == "START":
            self.StartButton.setText("STOP")
            self.StartButton.setIcon(
                QIcon(os.path.join(self.srcpath, "停止-1.png")))
            self.TrackButton.setEnabled(False)
            self.StartTime = datetime.now()
            self.StopTime = self.StartTime
            self.gap = self.StopTime - self.StartTime
            self.Timing = True
            self.LCD.setStyleSheet(
                "QLCDNumber{border:2px solidgreen;color:rgb(35, 107, 185 );}")
        else:
            # Stop 👉 Star(计时停止)
            self.StartButton.setText("START")
            self.StartButton.setIcon(
                QIcon(os.path.join(self.srcpath, "启动-2.png")))

            self.TrackButton.setEnabled(True)
            self.LCD.setStyleSheet(
                "QLCDNumber{border:2px solidgreen;color:rgb(102, 212, 209 );}")
            self.Timing = False
            # 更新时间
            self.StopTime = datetime.now()
            self.gap = self.StopTime - self.StartTime
            if self.gap.seconds/60 > 1:
                self.TrackButton.setStyleSheet(self.buttonStyle_2)

    def TrackLCD(self):
        # 有效记录
        self.TrackButton.setStyleSheet(self.buttonStyle_1)
        if int(self.gap.seconds) >= 0:
            self.gap = datetime.now() - datetime.now()
            self.__Writelog__()
        else:
            pass

    def UpdateLCD(self):
        if self.Timing:
            gap = datetime.now() - self.StartTime
            '''创建时间字符串'''
            time = QTime((gap.seconds/3600) %
                         24, (gap.seconds/60) % 60, gap.seconds % 60)
            text = time.toString('hh:mm:ss')
            self.LCD.display(text)
        else:
            self.LCD.display(datetime.now().strftime("%H:%M:%S"))

    def ManmalTrack(self):
        # 读取并打开单个文件,所以tuple索引为0。
        openfile_name = QFileDialog.getOpenFileName(
            self, '打开日志', '', 'Text Files (*.txt)')
        if openfile_name[0].strip() != "":
            os.system(openfile_name[0].strip())

    def AddPiece(self):
        # 手动单独添加
        self.mli = MultiInputDialog(self)
        self.mli.show()
        self.mli.signal_PieceInfo.connect(self.__WritePiece__)

    def __Writelog__(self):
        self.gap = self.StopTime - self.StartTime
        if int(self.gap.seconds) >= 2:
            text, ok = QInputDialog.getText(self, 'Track', 'What Did U DO?')
            if ok & (text.strip() != ""):
                f = open(os.path.join(self.logpath, r"log.txt"),
                         'a+', encoding='UTF-8')
                allLines = f.readlines()
                item = datetime.strftime(self.StartTime, "%Y-%m-%d %H:%M:%S") + \
                    "|" + datetime.strftime(self.StopTime, "%Y-%m-%d %H:%M:%S")
                item = item + "|" + str(int(self.gap.seconds/60))+"|"
                item = item + text
                allLines.append(item+"\n")
                f.writelines(allLines)
                f.close()
                # self.gap置零
                self.gap = datetime.now() - datetime.now()
                self.StartTime = datetime.now()
                self.StopTime = datetime.now()

    def __WritePiece__(self, info):
        if not isinstance(info, str):
            return
        elif len(info.strip()) < 10:
            return
        else:
            try:
                f = open(os.path.join(self.logpath, r"log.txt"),
                         'a+', encoding='UTF-8')
                allLines = f.readlines()
                allLines.append(info+"\n")
                f.writelines(allLines)
                f.close()
            except:
                pass


if __name__ == "__main__":
    import sys
    if 0 or 1:
        app = QApplication(sys.argv)
        if 1:
            form = ClockStatics_V1()
        else:
            form = ClockStatics()
        form.show()
        app.exec_()
