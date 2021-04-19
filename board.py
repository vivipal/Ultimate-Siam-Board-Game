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

        x,y = np.shape(self)
        view = np.empty((x,y),dtype=str)

        dir = ['^','>','v','<']

        for i in range(x):
            for j in range(y):
                if type(self[i,j]) == pion.Rhino :
                    view[i,j]='R'
                elif type(self[i,j]) == pion.Elephant :
                    view[i,j]='E'
                elif type(self[i,j]) == pion.Rocher :
                    view[i,j] = 'O'

                if view[i,j]!="":
                    view[i,j]+= dir[self[i,j].orientation//90]


        return view.__repr__()


    def move_check(L,direction):

        c_caillou = 0
        c_pour = 0
        c_contre = 0
        new_L = []

        for l in L:
            if l == None:
                break
            elif type(l) == Rocher:
                c_caillou += 1
            else:
                if l.orientation == direction:
                    c_pour += 1
                elif l.orientation == (direction + 180) % 360:
                    c_contre += 1
            new_L.append(l)

        y = True

        if c_contre > c_pour:
            y = False
        elif c_pour - c_contre - c_caillou < 0:
            y = False

        return y



    def move(self,animal,direction):
        """
        regarde si le mouvement désiré est réalisable et bouge les pions
        """
        x = animal.x
        y = animal.y
        size = np.shape(self)

        if direction == 0:
            L = self[ x , 0:y ].copy()
        elif direction == 90:
            L = self[ x:size[0] , y ].copy()
        elif direction == 180:
            L = self[ x , y:size[1] ].copy()
        elif direction == 270:
            L = self[ 0:x , y ].copy()
