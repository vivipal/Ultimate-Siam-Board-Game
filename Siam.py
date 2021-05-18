import pion
from board import Board
from interface import Ui_MainWindow
from ui import SiamGame

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)
window = SiamGame()
window.show()
app.exec_()
