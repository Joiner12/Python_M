#-*- coding:utf-8 -*-
'''
    统计分析功能区
    [1]文件是否存在https://www.cnblogs.com/jhao/p/7243043.html
'''

import sys
import os
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StaticsArea(QWidget):
    def __init__(self):
        super().__init__()
        self.srcpath = r"D:\Python_M\Code\PyTick\Src"
        self.logpath = r"D:\Python_M\Code\PyTick\Log"
        self.logOrg = ""
        print('initialization statics area')
        self.__ReadLog__()

    # 初始化UI界面
    def initUI(self):
        pass

    # 读取日志文本
    def __ReadLog__(self):
        if os.path.exists(os.path.join(self.logpath,r"log.txt")):
            f = open(os.path.join(self.logpath,r"log.txt"),'r',encoding='UTF-8')
            self.logOrg = f.readlines
            f.close()

    # 日志文本进行分析处理
    def __handleDetial__(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StaticsArea()
    ex.show()
    sys.exit(app.exec_())

