# -*- coding:utf-8 -*-
'''
    日志处理模块
'''
import pyqtgraph as pg
from datetime import datetime
import os
import sys
import pyqtgraph.examples
from PyQt5 import QtGui  # (the example applies equally well to PySide)


class LogMoudle():
    logDetailList = list()

    def __init__(self, logpath):
        # check file
        self.logpath = logpath
        fileflag = os.path.exists(logpath)
        if not fileflag:
            print('not a exist file')
    # [startkick,stopkick,duration,event]

    def GenList(self):
        try:
            with open(self.logpath, 'r', encoding='utf-8') as f:
                logDetail = f.readlines()
                f.close()
            for i in logDetail:
                deTemp = i.rstrip('\n')
                deTemp = deTemp.split('|')
                if len(deTemp) == 4:
                    CowOne = datetime.strptime(deTemp[0], "%Y-%m-%d %H:%M:%S")
                    CowTwo = datetime.strptime(deTemp[1], "%Y-%m-%d %H:%M:%S")
                    CowThree = int(deTemp[2])
                    deTemp[0] = CowOne
                    deTemp[1] = CowTwo
                    deTemp[2] = CowThree
                    self.logDetailList.append(deTemp)
        except:
            self.logDetailList = ['error' for i in range(4)]

    def DrawBar_1(self):
        pass

    def Graph_1(self):
        # Always start by initializing Qt (only once per application)
        app = QtGui.QApplication([])

        # Define a top-level widget to hold everything
        w = QtGui.QWidget()

        # Create some widgets to be placed inside
        btn = QtGui.QPushButton('press me')
        text = QtGui.QLineEdit('enter text')
        listw = QtGui.QListWidget()
        plot = pg.PlotWidget()

        # Create a grid layout to manage the widgets size and position
        layout = QtGui.QGridLayout()
        w.setLayout(layout)

        # Add widgets to the layout in their proper positions
        layout.addWidget(btn, 0, 0)   # button goes in upper-left
        layout.addWidget(text, 1, 0)   # text edit goes in middle-left
        layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
        # plot goes on right side, spanning 3 rows
        layout.addWidget(plot, 0, 1, 3, 1)

        # Display the widget as a new window
        w.show()

        # Start the Qt event loop
        app.exec_()


if __name__ == "__main__":
    ex = LogMoudle(r"D:\Codes\Python_M\Code\PyTick\Logs\log2.txt")
    ex.GenList()
    pyqtgraph.examples.run()
