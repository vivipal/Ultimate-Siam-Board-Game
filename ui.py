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

        # connect insertion button
        self.ui.pushButton_04d.clicked.connect(lambda : self.insert_piece(0,0))
        self.ui.pushButton_14.clicked.connect(lambda : self.insert_piece(1,0))
        self.ui.pushButton_34.clicked.connect(lambda : self.insert_piece(3,0))
        self.ui.pushButton_44d.clicked.connect(lambda : self.insert_piece(4,0))
        self.ui.pushButton_00l.clicked.connect(lambda : self.insert_piece(0,90))
        self.ui.pushButton_01.clicked.connect(lambda : self.insert_piece(1,90))
        self.ui.pushButton_02.clicked.connect(lambda : self.insert_piece(2,90))
        self.ui.pushButton_03.clicked.connect(lambda : self.insert_piece(3,90))
        self.ui.pushButton_04l.clicked.connect(lambda : self.insert_piece(4,90))
        self.ui.pushButton_00u.clicked.connect(lambda : self.insert_piece(0,180))
        self.ui.pushButton_10.clicked.connect(lambda : self.insert_piece(1,180))
        self.ui.pushButton_30.clicked.connect(lambda : self.insert_piece(3,180))
        self.ui.pushButton_40u.clicked.connect(lambda : self.insert_piece(4,180))
        self.ui.pushButton_40r.clicked.connect(lambda : self.insert_piece(0,270))
        self.ui.pushButton_41.clicked.connect(lambda : self.insert_piece(1,270))
        self.ui.pushButton_42.clicked.connect(lambda : self.insert_piece(2,270))
        self.ui.pushButton_43.clicked.connect(lambda : self.insert_piece(3,270))
        self.ui.pushButton_44r.clicked.connect(lambda : self.insert_piece(4,270))

        #connect direction selector buttons
        self.ui.up.clicked.connect(lambda :self.case_choice(self.ui.up))
        self.ui.down.clicked.connect(lambda :self.case_choice(self.ui.down))
        self.ui.left.clicked.connect(lambda :self.case_choice(self.ui.left))
        self.ui.right.clicked.connect(lambda :self.case_choice(self.ui.right))

        #add bg image to all case
        for i in range(self.ui.Board.count()):
                self.ui.Board.itemAt(i).widget().setStyleSheet("background-image : url(img/ground.jpeg)")


        #connect action selector buttons
        self.ui.RButton_insert.toggled.connect(self.choose_insert)
        self.ui.RButton_turn.toggled.connect(self.choose_turn)
        self.ui.RButton_move_turn.toggled.connect(self.move_turn_piece)


        self.ui.textBrowser.setText("Au tour des Elephants")




        self.choice_raz()



    def case_choice(self,button):

        y = button.x()%70//6 - 1
        x = button.y()%70//6 - 1

        action = self.get_action()

        if action == 1 :
            if self.selected_piece == None  :
                self.selected_piece = self.board[x,y]

                if self.board.verify_piece(self.selected_piece) :
                    for button in self.ui.direction_selector.buttons():
                        button.show()
                else :
                    print("TUPEUXPASS SALOOP")
                    self.choice_raz()
                    return


            else :
                button_name = button.objectName()
                if button_name == 'up':
                    new_dir = 0
                elif button_name == 'down':
                    new_dir = 180
                elif button_name == 'right' :
                    new_dir = 90
                elif button_name == 'left' :
                    new_dir = 270

                self.turn_piece(self.selected_piece,new_dir)



        # button.setStyleSheet("background-image : url(rhino.jpeg);")
        # button.setIcon(QtGui.QIcon('rhino.jpeg'))


        # self.rhinopix = QtGui.QPixmap("rhino.jpeg")
        # button.setIcon(QtGui.QIcon(self.rhinopix))
        # button.setIconSize(QtCore.QSize(70,70))


    def verify_piece(self,piece):

        if self.board.tour_elephant == True and type(piece)==pion.Elephant :
            print("OKKKKK")


    def choice_raz(self):

        #hide all optionnal buttons
        for button in self.ui.direction_insert.buttons():
            button.hide()
        for button in self.ui.direction_selector.buttons():
            button.hide()

        #no piece is selected
        self.selected_piece = None

    def uncheck_action_selector(self):
        """
        décoche toutes les cases de sélection d'action
        """

        for i in range(self.ui.ActionSelector.count()):
            self.ui.ActionSelector.itemAt(i).widget().setAutoExclusive(False)
            self.ui.ActionSelector.itemAt(i).widget().setChecked(False)
            self.ui.ActionSelector.itemAt(i).widget().setAutoExclusive(True)


    def end_turn(self):

        self.uncheck_action_selector()

        self.board.next_turn()

        self.choice_raz()
        self.ui.textBrowser.append("Tour fini")
        self.ui.textBrowser.append("")
        self.ui.textBrowser.append("----------------")
        self.ui.textBrowser.append("")

        if self.board.tour_elephant :
            self.ui.textBrowser.append("Au tour des Elephants")
        else :
            self.ui.textBrowser.append("Au tour des Rhinocéros")

    def choose_insert(self):
        self.choice_raz()

        if self.board.check_insert():
            for button in self.ui.direction_insert.buttons():
                button.show()
        else :
            self.uncheck_action_selector()
            self.ui.textBrowser.append("Tu ne peux pas ajouter une nouvelle pièce.")

    def choose_turn(self):
        self.choice_raz()

    def insert_piece(self,pos,dir=None):
        self.board.insert(dir,pos)
        self.end_turn()

    def turn_piece(self,piece,dir):
        piece.turn(dir)
        print(self.board)
        self.end_turn()

    def move_turn_piece(self):

        self.choice_raz()

        print('u want to move & turn a piece')


    def get_action(self):
        """
        return the action selected : 0 --> insert
                                     1 --> turn
                                     2 --> move and turn
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
