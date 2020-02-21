# -*- coding:utf-8 -*-

'''
    supplement of mainwindow
'''
import sys
from Ui_PyTick import Ui_MainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

# "D:\\Codes\\Python_M\\Code\\PyTick\\Src\\Deer.ico"


class UiSupplement(Ui_MainWindow, QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.HandleMainWindow_1()
        print('main window init')

    def paintEvent(self, event):
        bgQp = QPainter(self)
        file_path = os.path.abspath(__file__)
        img_src = os.path.abspath(os.path.join(
            os.path.join(file_path, '../..'), 'Src'))
        # mainBackGround = os.path.join(
        #     img_src, 'Background-1.jpg')
        mainBackGround = "D:\\Codes\\Python_M\\Code\\PyTick\\Src\\Background-1.jpg"
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)

    def HandleMainWindow_1(self):
        self.setFixedSize(1024, 683)
        # self.setWindowFlag(Qt.WindowMinimizeButtonHint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_s = UiSupplement()
    ma = QMainWindow()
    ui_s.setupUi(ma)
    ma.show()
    sys.exit(app.exec_())
