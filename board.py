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
        view = np.empty((x,y),dtype='<U2')


        dir = ['^','>','v','<']

        for i in range(x):
            for j in range(y):
                if type(self[i,j]) == pion.Rhino :
                    view[i,j]='R'
                elif type(self[i,j]) == pion.Elephant :
                    view[i,j]='E'
                elif type(self[i,j]) == pion.Rocher :
                    view[i,j] = 'O'
                else:
                    view[i,j]="  "

                if view[i,j]!="  ":
                    view[i,j]+= dir[self[i,j].orientation//90]


        return view.__repr__()


    def nb_rhino(self):
        """
        compte le nombre de rhino
        """
        nb = 0
        for p in self.ravel():
            if type(p) == pion.Rhino:
                nb += 1
        return nb

    def nb_elephant(self):
        """
        compte le nombre d'éléphant
        """
        nb = 0
        for p in self.ravel():
            if type(p) == pion.Elephant:
                nb += 1
        return nb

    def nb_rocher(self):
        """
        compte le nombre de rocher
        """
        nb = 0
        for p in self.ravel():
            if type(p) == pion.Rocher:
                nb += 1
        return nb


    def move_check(self,L,direction):
        """
        à partir de la liste créée par move(), regarde si le mouvement demandé est possible
        """

        c_caillou = 0
        c_pour = 0
        c_contre = 0
        new_L = []


        for l in L:
            if l == None:
                break
            elif type(l) == pion.Rocher:
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

        return new_L, y


    def set_pion(self, pion):
        """
        ajoute un pion sur le plateau de jeu
        """
        self[pion.x, pion.y] = pion

    def clear(self):
        """
        vide toutes les cases de Board (remplace par None)
        """

        x,y = np.shape(self)

        for i in range(x):
            for j in range(y):
                self[i,j] = None


    def update(self):
        """
        met à jour Board selon les nouvelles coordonnées des pions
        """
        copy = self.copy()
        self.clear()
        for p in copy.ravel():
            if p != None:
                self[p.x, p.y] = p


    def move(self,animal,direction):
        """
        fait bouger le pion dans la direction demandée, pousse les pions devant si possible
        """

        x = animal.x
        y = animal.y
        size = np.shape(self)

        if direction == 270:
            L = self[ x , 0:y+1][::-1].copy()

        elif direction == 180:
            L = self[ x:size[0]+1 , y ].copy()

        elif direction == 90:
            L = self[ x, y:size[1]+1 ].copy()

        elif direction == 0:
            L = self[ 0:x+1 , y][::-1].copy()

        L=np.array(L)
        print(L)
        new_L, y = self.move_check(L, direction)

        for pion_bouge in new_L:
            pion_bouge.move(direction)

        self.update()



if __name__=='__main__' :
    a = Board((5,5),dtype=object)
    v=pion.Rhino(2,3,90)
    v2=pion.Rhino(2,4,0)
    v3=pion.Rhino(1,4,90)
    u=pion.Elephant(1,0,180)
    u2=pion.Elephant(4,4,0)
    a[2,3]=v
    a[2,4]=v2
    a[1,4]=v3
    a[1,0]=u
    a[4,4]=u2
