import numpy as np
import pion

class Board(np.ndarray):
    '''
    Classe représentant le plateau de jeu et gérant le déroulement de la partie
    '''

    def __init__(self,size,dtype=object):
        """
        size tuple represent the size of the board game.
        """


    def __str__(self):
        """
        affichage simplifié du plateau de jeu
        """
        view = self[:]
        view[type(view) == pion.Rhino] = "R"
        view[type(view) == pion.Elephant] = "E"
        view[type(view) == pion.Rocher] = "O"
        view[view==None] = ""

        return view


    def check(animal, direction):
        """
        regarde si le mouvement désiré est réalisable
        """
        x = animal.x
        y = animal.y

        c_pour = 1
        c_contre = 0
        c_rocher = 0
        i = 1

        if direction == 0:
            while 0<= y-i <=4 and self[x,y-i] != None:
                obs = self[x,y-i]
                if type(obs) == Rocher:
                    c_rocher += 1
                else:
                    if orientation == (direction + 180) % 360 :
                        c_contre += 1
                    elif orientation == direction :
                        c_pour += 1


    def
