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
        affichage sipmifié du plateau de jjeu et
        """
        view = self[:]
        view[type(view) == pion.Rhino] = "R"
        view[type(view) == pion.Elephant] = "E"
        view[type(view) == pion.Rocher] = "O"
        view[view=None] = ""

        return view


    def check(animal, direction):
        """
        bouge un ou plusieurs animaux dans une direction spécifique si cela est possible
        """
        x = animal.x
        y = animal.y

        c_pour = 1
        c_contre = 0
        c_rocher = 0
        i = 1
        # sens = -1 + (animal.ortientation=="E" or animal.orientation=="S")*2   # valeur d'incrémentation, 1 si vers Nord ou Est, -1 si vers Sud ou Ouest
        #
        # if animal.orientation=="N" or animal.orientation=="S":
        #     while 0 <= y+sens*i <= 4 and self[x,y+sens*i]!=None:


    def 
