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
        self.ui.case00.clicked.connect(lambda : self.case_choice(self.ui.case00))
        self.ui.case01.clicked.connect(lambda : self.case_choice(self.ui.case01))
        self.ui.case02.clicked.connect(lambda : self.case_choice(self.ui.case02))
        self.ui.case03.clicked.connect(lambda : self.case_choice(self.ui.case03))
        self.ui.case04.clicked.connect(lambda : self.case_choice(self.ui.case04))
        self.ui.case10.clicked.connect(lambda : self.case_choice(self.ui.case10))
        self.ui.case11.clicked.connect(lambda : self.case_choice(self.ui.case11))
        self.ui.case12.clicked.connect(lambda : self.case_choice(self.ui.case12))
        self.ui.case13.clicked.connect(lambda : self.case_choice(self.ui.case13))
        self.ui.case14.clicked.connect(lambda : self.case_choice(self.ui.case14))
        self.ui.case20.clicked.connect(lambda : self.case_choice(self.ui.case20))
        self.ui.case21.clicked.connect(lambda : self.case_choice(self.ui.case21))
        self.ui.case22.clicked.connect(lambda : self.case_choice(self.ui.case22))
        self.ui.case23.clicked.connect(lambda : self.case_choice(self.ui.case23))
        self.ui.case24.clicked.connect(lambda : self.case_choice(self.ui.case24))
        self.ui.case30.clicked.connect(lambda : self.case_choice(self.ui.case30))
        self.ui.case31.clicked.connect(lambda : self.case_choice(self.ui.case31))
        self.ui.case32.clicked.connect(lambda : self.case_choice(self.ui.case32))
        self.ui.case33.clicked.connect(lambda : self.case_choice(self.ui.case33))
        self.ui.case34.clicked.connect(lambda : self.case_choice(self.ui.case34))
        self.ui.case40.clicked.connect(lambda : self.case_choice(self.ui.case40))
        self.ui.case41.clicked.connect(lambda : self.case_choice(self.ui.case41))
        self.ui.case42.clicked.connect(lambda : self.case_choice(self.ui.case42))
        self.ui.case43.clicked.connect(lambda : self.case_choice(self.ui.case43))
        self.ui.case44.clicked.connect(lambda : self.case_choice(self.ui.case44))

        #add bg image to all case
        for i in range(self.ui.Board.count()):
                self.ui.Board.itemAt(i).widget().setStyleSheet("background-image : url(ground.jpeg)")

        self.rhinopix = QtGui.QPixmap("rhino.jpeg")



    def case_choice(self,button):

        x = button.x()%70//6 - 1
        y = button.y()%70//6 - 1

        print(x,y)

        # button.setStyleSheet("background-image : url(rhino.jpeg);")
        # button.setIcon(QtGui.QIcon('rhino.jpeg'))


        # self.rhinopix = QtGui.QPixmap("rhino.jpeg")
        button.setIcon(QtGui.QIcon(self.rhinopix))
        button.setIconSize(QtCore.QSize(70,70))

        self.turn_piece()


    def insert_piece(self):
        print('u want to insert a piece')

    def turn_piece(self):

        self.rhinopix = self.rhinopix.transformed(QtGui.QTransform().rotate(90))

        print('u want to turn a piece')

    def move_turn_piece(self):
        print('u want to move & turn a piece')


    def get_action(self):
        """
        return the action selected : 0 --> insert
                                     1 --> turn
                                     3 --> move and turn
                                     -1 --> no action selected

        """
        for i in range(self.ui.ActionSelector.count()):
            if self.ui.ActionSelector.itemAt(i).widget().isChecked():
                return i
        return -1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SiamGame()
    window.show()
    app.exec_()
