import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from interface import Ui_MainWindow

# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre
# créée avec QT Designer. Nous configurons après l'interface utilisateur
# dans le constructeur (la méthode init()) de notre classe

class SiamGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #connect case button
        self.ui.case00.clicked.connect(lambda : self.case_choice(0,0))
        self.ui.case01.clicked.connect(lambda : self.case_choice(0,1))
        self.ui.case02.clicked.connect(lambda : self.case_choice(0,2))
        self.ui.case03.clicked.connect(lambda : self.case_choice(0,3))
        self.ui.case04.clicked.connect(lambda : self.case_choice(0,4))
        self.ui.case10.clicked.connect(lambda : self.case_choice(1,0))
        self.ui.case11.clicked.connect(lambda : self.case_choice(1,1))
        self.ui.case12.clicked.connect(lambda : self.case_choice(1,2))
        self.ui.case13.clicked.connect(lambda : self.case_choice(1,3))
        self.ui.case14.clicked.connect(lambda : self.case_choice(1,4))
        self.ui.case20.clicked.connect(lambda : self.case_choice(2,0))
        self.ui.case21.clicked.connect(lambda : self.case_choice(2,1))
        self.ui.case22.clicked.connect(lambda : self.case_choice(2,2))
        self.ui.case23.clicked.connect(lambda : self.case_choice(2,3))
        self.ui.case24.clicked.connect(lambda : self.case_choice(2,4))
        self.ui.case30.clicked.connect(lambda : self.case_choice(3,0))
        self.ui.case31.clicked.connect(lambda : self.case_choice(3,1))
        self.ui.case32.clicked.connect(lambda : self.case_choice(3,2))
        self.ui.case33.clicked.connect(lambda : self.case_choice(3,3))
        self.ui.case34.clicked.connect(lambda : self.case_choice(3,4))
        self.ui.case40.clicked.connect(lambda : self.case_choice(4,0))
        self.ui.case41.clicked.connect(lambda : self.case_choice(4,1))
        self.ui.case42.clicked.connect(lambda : self.case_choice(4,2))
        self.ui.case43.clicked.connect(lambda : self.case_choice(4,3))
        self.ui.case44.clicked.connect(lambda : self.case_choice(4,4))

    def insert_piece(self):
        print('u want to insert a piece')

        print(self.get_action())

    def case_choice(self,x,y):
        print("case en {},{}".format(x,y))

    def turn_piece(self):
        print('u want to turn a piece')

    def move_turn_piece(self):
        print('u want to move & turn a piece')

    def get_action(self):
        for i in range(self.ui.ActionSelector2.count()):
            if self.ui.ActionSelector2.itemAt(i).widget().isChecked():
                return i
        return -1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SiamGame()
    window.show()
    app.exec_()
