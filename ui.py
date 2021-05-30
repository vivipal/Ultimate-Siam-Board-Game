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



        #connect action selector buttons
        self.ui.RButton_insert.toggled.connect(self.choose_insert)
        self.ui.RButton_turn.toggled.connect(self.choose_turn)
        self.ui.RButton_move_turn.toggled.connect(self.choose_move_turn_piece)


        self.ui.textBrowser.setText("Au tour des Elephants")

        self.update_ui()


        self.choice_raz()



    def case_choice(self,button):

        """
        methode appellé lors d'un appui sur une case
        si une action (bouger ou tourner) est selectionnée, ça lance la fonction correspondante
        """

        y = button.x()%70//6 - 1
        x = button.y()%70//6 - 1

        action = self.get_action()

        if action == 1 :
            self.turn(x,y,button)
        elif action==2 :
            self.move(x,y,button)



    def choice_raz(self):

        """
        cache tous les boutons inutile (choix direction et choix insertion)
        et remet à NULL la variable de choix de piece
        """

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
        """
        met fin à un tour :
            - met a jour l'affichage du plateau
            - décoche l'action selectionné
            - raz des choix
            - met a jour la variable du joueur qui doit jouer
            - affiche infos dans l'UI
        """

        self.update_ui()

        self.uncheck_action_selector()
        self.choice_raz()

        self.board.next_turn()

        self.ui.textBrowser.append("Tour fini")
        self.ui.textBrowser.append("")
        self.ui.textBrowser.append("----------------")
        self.ui.textBrowser.append("")

        if self.board.tour_elephant :
            self.ui.textBrowser.append("Au tour des Elephants")
        else :
            self.ui.textBrowser.append("Au tour des Rhinocéros")

    def choose_insert(self):

        """
        raz des choix deja fait
        et affiche les boutons pour inserer une piece ssi le joueur peut encore en ajouter
        """
        self.choice_raz()

        if self.board.check_insert():
            for button in self.ui.direction_insert.buttons():
                button.show()
        else :
            self.uncheck_action_selector()
            self.ui.textBrowser.append("Tu ne peux pas ajouter une nouvelle pièce.")

    def choose_turn(self):
        """
        raz des choix deja fait
        """
        self.choice_raz()

    def turn(self,x,y,button):
        """
        méthode appellé lorsque l'on veut tourner une piece
            -dans un premier temps si aucune piece n'a été sélectionné avant, on stocke la piece
            -ensuite lors du 2eme appel on fait tourner la piece
        """

        if self.selected_piece == None  : #si aucune piece n'a deja était selectionné
            self.selected_piece = self.board[x,y]

            if self.board.verify_piece(self.selected_piece) :
                for button in self.ui.direction_selector.buttons():
                    button.show()
            else :
                self.ui.textBrowser.append("Cette piece ne t'appartient pas")
                self.ui.textBrowser.append("Recommencez votre tour")

                self.choice_raz()
                return
        else :  #si une piece a été selectionné on regarde dans quelle direction la tourner et on la tourne
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


    def insert_piece(self,pos,dir=None):
        """
        on insert la piece et on  met fin au tour
        """

        self.board.insert(dir,pos)
        self.end_turn()

    def turn_piece(self,piece,dir):
        """
        on tourne la piece et on met fin au tour
        """

        piece.turn(dir)
        print(self.board)
        self.end_turn()

    def choose_move_turn_piece(self):
        """
        raz des choix deja fait
        """
        self.choice_raz()

    def move(self,x,y,button):
        """
        méthode appellée lorsque l'on veut bouger une piece
            -dans un premier temps si aucune piece n'a été sélectionné avant, on stocke la piece
            -ensuite lors du 2eme appel on fait bouger la piece
        """
        if self.selected_piece == None  :#si aucune piece n'a deja était selectionné
            self.selected_piece = self.board[x,y]

            if self.board.verify_piece(self.selected_piece) :
                for button in self.ui.direction_selector.buttons():
                    button.show()
            else :
                self.ui.textBrowser.append("Cette piece ne t'appartient pas")
                self.choice_raz()
                return
        else :  #si une piece a été selectionné on regarde dans quelle direction l'avancer et on la bouge
            button_name = button.objectName()
            try :
                if button_name == 'up':
                    new_dir = 0
                elif button_name == 'down':
                    new_dir = 180
                elif button_name == 'right' :
                    new_dir = 90
                elif button_name == 'left' :
                    new_dir = 270
                self.move_piece(self.selected_piece,new_dir)
            except :
                self.ui.textBrowser.append("Choisir la direction avec les cases prévus")
                self.ui.textBrowser.append("Recommencer votre tour")
                self.choice_raz()


    def move_piece(self,piece,dir):
        """
        Bouge une piece si le mouvement peut se faire
        """
        info_move = self.board.move(piece,dir)
        if info_move[1]:  #regarde si le mouvement a pu se faire ou pas
            print(self.board)
            self.end_turn()
        else :
            self.ui.textBrowser.append("Tu ne peux pas faire ce mouvement")
            self.ui.textBrowser.append("Recommencez votre tour")
            self.choice_raz()

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

    def update_ui(self):
        """
        place les images de rocher/elephant/rhino en fonction de leur psoition sur le plateau
        """

        for i,elm in enumerate(self.board.ravel()):

            button = self.ui.Board.itemAtPosition(i//5,i%5).widget()

            if elm !=None :
                img_path = "img/{}.jpeg".format(str(elm))

                pixmap = QtGui.QPixmap(img_path)

                try :
                    orientation = elm.orientation
                    transform = QtGui.QTransform().rotate(orientation-90)
                    pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
                except:
                    pass

                button.setIcon(QtGui.QIcon(pixmap))
                button.setIconSize(QtCore.QSize(70,70))
            else :

                pixmap = QtGui.QPixmap('img/ground.jpeg')
                button.setIcon(QtGui.QIcon(pixmap))
                button.setIconSize(QtCore.QSize(70,70))
