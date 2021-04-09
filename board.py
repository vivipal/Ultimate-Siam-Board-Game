import numpy as np

class Board(np.ndarray):
    '''

    Classe représentant le plateau de jeuet gérant le déroulement de la partie

    '''
    def __init__(self,size=(5,5)):
        """
        size tuple represent the size of the board game.
        """

        self.width, self.height = size



import numpy as np


class C(np.ndarray):



    def __init__(self,t,dtype):
        super().__init__()



a=C((5,5),dtype=object)

print(a)
