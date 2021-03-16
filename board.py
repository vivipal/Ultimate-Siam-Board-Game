

class Board():
    '''

    Classe représentant le plateau de jeuet gérant le déroulement de la partie

    '''
    def __init__(self,size=(5,5)):
        """
        size tuple represent the size of the board game.
        """

        self.width, self.height = size
