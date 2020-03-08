# -*- coding:utf-8 -*-
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from numpy import random


class KeyMouse(QWidget):
    # 初始化
    def __init__(self):
        super().__init__()
        self.setWindowTitle("给我抖~")
        self.label = QLabel("KEYSSCAN", self)
        self.initUI()
    # 设置窗口的参数

    def initUI(self):
        # 设置背景图片
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(
            QPixmap(r"D:\Codes\Python_M\Code\PyTick\Src\Deer-2.png")))
        self.setPalette(palette)
        self.show()
    # 检测键盘回车按键，函数名字不要改，这是重写键盘事件

    def keyPressEvent(self, event):
        # style_1 = {color: (random.randint(0, 255), random.randint(
        #     0, 255), random.randint(0, 255))}
        self.label.setText(str(event.key()))
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)
        pe.setColor(QPalette.Window, Qt.blue)
        # pe.setColor(QPalette.Background,Qt.blue)
        self.label.setPalette(pe)

        self.label.setFont(
            QFont("Roman times", random.randint(100, 200), QFont.Bold))
        self.label.adjustSize()
        self.label.move(random.randint(0, 400), random.randint(0, 200))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyMouse()
    sys.exit(app.exec_())
