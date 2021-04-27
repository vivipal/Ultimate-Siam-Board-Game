import numpy as np
import pion

class Board(np.ndarray):
    '''
    Classe représentant le plateau de jeu
    '''

    def __init__(self,size,dtype=object):
        """
        size tuple represent the size of the board game.
        """

    def __str__(self):
        """
        affichage simplifié du plateau de jeu
        """
        print("-----------------------")
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
                    view[i,j] ='##'
                else:
                    view[i,j]="  "

                if view[i,j]!="  " and view[i,j]!='##':
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
        new_L, y = self.move_check(L, direction)

        W = []

        if y:
            for pion_bouge in new_L:
                pion_bouge.move(direction)
                if type(pion_bouge)==pion.Rocher and not (0>pion_bouge.x>4 and 0>pion_bouge.y>4):
                    for pion_win in new_L[::-1]:
                        if type(pion_bouge)!=pion.Rocher and pion_win.orientation == direction:
                            W = [type(pion_win)]

        self.update()

        return new_L, y, W

    def insert(self,tour_elep,direction,x):
        """
        Insère un nouveau pion sur le plateau, pousse les autres si nécessaire
        """
        if direction == 270:
            L2 = self[x,:][::-1].copy()
            y=4

        elif direction == 180:
            L2 = self[:,x].copy()
            y=x
            x=0

        elif direction == 90:
            L2 = self[x,:].copy()
            y=0

        elif direction == 0:
            L2 = self[:,x][::-1].copy()
            y=x
            x=4

        L2 = np.array(L2)
        L2 = np.insert(L2,0,[pion.Rhino(0,0,direction)])       # on rajoute un animal dans le sens de la marche pour que move_check() fonctionne
        new_L2, check = self.move_check(L2, direction)


        if check:
            for pion_bouge in new_L2[1:]:            # mais on ne bouge pas l'animal rajouté
                pion_bouge.move(direction)
            self.update()
            if tour_elep == True:
                p = pion.Elephant(x,y,direction)
            else:
                p = pion.Rhino(x,y,direction)
            self.set_pion(p)


        return check, new_L2, p


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

        if len(new_L)>1 and new_L[0].orientation != direction:
            y = False

        if len(new_L)>1:
            if c_contre >= c_pour:
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
            if p != None and 0<=p.x<=4 and 0<=p.y<=4:
                self[p.x, p.y] = p


if __name__=='__main__' :
    a = Board((5,5),dtype=object)
    a.set_pion(pion.Rhino(0,0,90))
    a.set_pion(pion.Rhino(0,1,90))
    a.set_pion(pion.Rocher(0,2))
    a.set_pion(pion.Rhino(0,3,270))
    print(a)
    #a[2,2].turn(270)
    a.move(a[0,0],90)
    print(a)
    print(type(a[0,1]))
