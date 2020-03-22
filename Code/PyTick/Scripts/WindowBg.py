# -*- coding:utf-8 -*-
'''
    设置mainwindow背景图
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
import sys
import os


class BgClass(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('修改背景')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())

        if False:
            # todo 1 设置背景颜色
            painter.setBrush(Qt.transparent)
            painter.drawRect(self.rect())
        else:
            # todo:使用相对路径背景文件不生效
            file_path = os.path.abspath(__file__)
            img_src = os.path.abspath(os.path.join(
                os.path.join(file_path, '../..'), 'Src'))
            bgfile = os.path.join(img_src, 'Background-2.jpg')
            pixBg = QPixmap(bgfile)

            painter.drawPixmap(self.rect(), pixBg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bg = BgClass()
    bg.show()
    sys.exit(app.exec_())
