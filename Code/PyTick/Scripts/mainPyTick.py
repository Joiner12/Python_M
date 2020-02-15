# -*- coding:utf-8 -*-

import PyTick
from PyQt5.QtWidgets import QApplication, QWidget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ru = PyTick.Ui_MainWindow()
    ru.show()
    sys.exit(app.exec_())
