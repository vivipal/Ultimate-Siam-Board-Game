
class Pion():
    '''
    Classe décrivant les pions du jeu
    '''

    def __init__(self, x, y):
        '''
        Crée un pion aux coordonnées désirées
        '''
        self.__coords = x, y

    @property
    def coords(self):
        """
        Les coordonnées du pion sur le plateau de jeu
        """
        return self.__coords

    @coords.setter
    def coords(self, nouv_coords):
        """
        Met à jour les coordonnées du pion
        """
        x, y = new_coords
        self.__coords = (x, y)


    @property
    def x(self):
        """
        x: nombre entier
            abscisse du pion
        """
        return self.coords[0]

    @property
    def y(self):
        """
        y: nombre entier
            ordonee du pion
        """
        return self.coords[1]



class Rocher(Pion):

    '''
    Classe representant les Rochers
    '''

    def __init__(self,x,y):

        super().__init__(x, y)


class Animal(Pion):

    '''
    Classe representatn les Animaux (Rhino/Elephant)
    '''

    def __init__(self,x,y,espece,orientation ):

        '''
        ----------
        Parametre:

        x: nombre entier
            abscisse du pion
        y: nombre entier
            ordonnee du pion
        espece: caractere
            'R' pour un Rhino
            'E' pour un Elephant
        orientation: caractere
            'N','S','E','O' pour respectivement nord, sud, est ,ouest

        ----------
        '''


        super().__init__(x,y)

        self.__orientation = orientation
        self.espece = espece
