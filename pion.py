import numpy

class Pion():
    '''
    Classe décrivant les pions (Elephant, Rhino, Caillou)
    '''

    def __init__(self, abscisse, ordonnee):
        '''
        Crée un pion aux coordonnées désirées
        '''
        self.coords = abscisse, ordonnee
