import pion
from board2 import Board
from interface import Ui_MainWindow
from ui import SiamGame

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic


#create a new 5x5 board
board = Board((5,5),dtype=object)


app = QtWidgets.QApplication(sys.argv)
window = SiamGame(board)
window.show()
app.exec_()
