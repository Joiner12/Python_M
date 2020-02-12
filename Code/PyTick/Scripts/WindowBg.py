# -*- coding:utf-8 -*-
'''
    设置mainwindow背景图

    Reference:
    [1]<修改背景图> https://blog.csdn.net/jia666666/article/details/81874045
    [2]<通过PYQT调整>https://blog.csdn.net/qq_41784559/article/details/88601084
    [3]<路径问题>https://www.cnblogs.com/wangyanyan/p/7440685.html
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPixmap
import sys
import os


class BgClass(QWidget):
    def init(self):
        super().__init__()
        self.setWindowTitle('修改背景')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())

        if False:
            # todo 1 设置背景颜色
            painter.setBrush(Qt.green)
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
