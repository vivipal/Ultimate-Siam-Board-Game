# import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from interface import Ui_MainWindow


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre
# créée avec QT Designer. Nous configurons après l'interface utilisateur
# dans le constructeur (la méthode init()) de notre classe

class SiamGame(QtWidgets.QMainWindow):
    def __init__(self,board):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.board = board


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


        self.ui.pushButton_00l.clicked.connect(lambda : self.insert_piece(0,0,90))
        self.ui.pushButton_00u.clicked.connect(lambda : self.insert_piece(0,0,180))
        self.ui.pushButton_01.clicked.connect(lambda : self.insert_piece(0,1))
        self.ui.pushButton_02.clicked.connect(lambda : self.insert_piece(0,2))
        self.ui.pushButton_03.clicked.connect(lambda : self.insert_piece(0,3))
        self.ui.pushButton_04d.clicked.connect(lambda : self.insert_piece(0,4,0))
        self.ui.pushButton_04l.clicked.connect(lambda : self.insert_piece(0,4,90))
        self.ui.pushButton_10.clicked.connect(lambda : self.insert_piece(1,0))
        self.ui.pushButton_14.clicked.connect(lambda : self.insert_piece(1,4))
        self.ui.pushButton_30.clicked.connect(lambda : self.insert_piece(3,0))
        self.ui.pushButton_34.clicked.connect(lambda : self.insert_piece(3,4))
        self.ui.pushButton_40r.clicked.connect(lambda : self.insert_piece(4,0,270))
        self.ui.pushButton_40u.clicked.connect(lambda : self.insert_piece(4,0,180))
        self.ui.pushButton_41.clicked.connect(lambda : self.insert_piece(4,1))
        self.ui.pushButton_42.clicked.connect(lambda : self.insert_piece(4,2))
        self.ui.pushButton_43.clicked.connect(lambda : self.insert_piece(4,3))
        self.ui.pushButton_44d.clicked.connect(lambda : self.insert_piece(4,4,0))
        self.ui.pushButton_44r.clicked.connect(lambda : self.insert_piece(4,4,270))

        #add bg image to all case
        for i in range(self.ui.Board.count()):
                self.ui.Board.itemAt(i).widget().setStyleSheet("background-image : url(img/ground.jpeg)")


        self.ui.RButton_insert.toggled.connect(self.choose_insert)
        self.ui.RButton_turn.toggled.connect(self.turn_piece)
        self.ui.RButton_move_turn.toggled.connect(self.move_turn_piece)

        for button in self.ui.direction_insert.buttons():
            button.hide()



    def case_choice(self,button):

        y = button.x()%70//6 - 1
        x = button.y()%70//6 - 1

        print(x,y)

        action = self.get_action()

        if action >=0 :
            if action == 0 :
                self.insert_piece(x,y)

        # button.setStyleSheet("background-image : url(rhino.jpeg);")
        # button.setIcon(QtGui.QIcon('rhino.jpeg'))


        # self.rhinopix = QtGui.QPixmap("rhino.jpeg")
        # button.setIcon(QtGui.QIcon(self.rhinopix))
        # button.setIconSize(QtCore.QSize(70,70))


    def choose_insert(self):

        for button in self.ui.direction_insert.buttons():
            button.show()

    def insert_piece(self,y,x,dir=None):

        if dir == None:
            if x==0:
                dir = 180
            elif x==4:
                dir = 0
            elif y == 0:
                dir = 90
            elif y==4:
                dir = 270

        self.board.insert2(x,y,dir)


    def turn_piece(self):
        for button in self.ui.direction_insert.buttons():
            button.hide()

        # self.rhinopix = self.rhinopix.transformed(QtGui.QTransform().rotate(90))

        print('u want to turn a piece')

    def move_turn_piece(self):
        for button in self.ui.direction_insert.buttons():
            button.hide()
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

    ingame = True
    tour_elep = True

    plateau = board.Board((5,5),dtype=object)

    app = QtWidgets.QApplication(sys.argv)
    window = SiamGame(plateau)
    window.show()
    app.exec_()
