# from board import Board

class Pion():
    '''
    Classe décrivant les pions (Elephant, Rhino, Caillou)
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
    def coords(self, new_coords):
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

    @x.setter
    def x(self,new_x):
        self.coords = (new_x,self.y)

    @property
    def y(self):
        """
        y: nombre entier
            ordonee du pion
        """
        return self.coords[1]

    @y.setter
    def y(self,new_y):
        self.coords = (self.x,new_y)

    def move(self, direction):
        old_x = self.x
        old_y = self.y
        if direction == 270:
            self.y = old_y - 1
        elif direction == 90:
            self.y = old_y + 1
        elif direction == 180:
            self.x = old_x + 1
        else:
            self.x = old_x - 1

class Rocher(Pion):

    '''
    Classe representant les Rochers
    '''

    def __init__(self,x,y):

        super().__init__(x, y)

    def __str__(self) :
        return 'rocher'

class Animal(Pion):

    '''
    Classe representatn les Animaux (Rhino/Elephant)
    '''

    def __init__(self,x,y,orientation,espece):

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
            0, 180, 90, 270 pour respectivement nord, sud, est ,ouest

        ----------
        '''


        super().__init__(x,y)

        self.__orientation = orientation
        self.espece = espece


    @property
    def orientation(self):
        return self.__orientation


    @orientation.setter
    def orientation(self,new_orientation):
        self.__orientation = new_orientation


    def turn(self, new_orientation):
        self.orientation = new_orientation



class Rhino(Animal):

    '''
    Classe representant les Rhinoceros
    '''

    def __init__(self,x,y,orientation):

        super().__init__(x,y,orientation,'R')

    def __str__(self):
        return "rhino"

class Elephant(Animal):

    '''
    Classe representant les Elephant
    '''

    def __init__(self,x,y,orientation):

        super().__init__(x,y,orientation,'E')

    def __str__(self):
        return "eleph"
