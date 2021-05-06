import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre
# créée avec QT Designer. Nous configurons après l'interface utilisateur
# dans le constructeur (la méthode init()) de notre classe

class SiamGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #connect button
        self.ui.Button_insert.clicked.connect(self.insert_piece)
        self.ui.Button_turn.clicked.connect(self.turn_piece)
        self.ui.Button_move_turn.clicked.connect(self.move_turn_piece)

    def insert_piece(self):
        print('u want to insert a piece')

    def turn_piece(self):
        print('u want to turn a piece')

    def move_turn_piece(self):
        print('u want to move & turn a piece')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SiamGame()
    window.show()
    app.exec_()
