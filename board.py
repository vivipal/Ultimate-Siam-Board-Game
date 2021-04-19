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
