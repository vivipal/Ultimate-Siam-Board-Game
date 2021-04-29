import numpy as np
import pion


def move_check_delete_none(L):
    """
    transforme la liste créée par move() en ne gardant que les pions susceptibles de bouger
    """
    L_return = []
    for l in L:
        if l!=None:
            L_return.append(l)
        else:
            break
    L_return = np.array(L_return)
    return L_return

def move_check_contre(L,direction):
    """
    vérifie s'il reste des animaux s'opposant au mouvement dans la liste
    """
    y = False
    for p in L:
        if type(p)!=pion.Rocher and p.orientation==(direction + 180) % 360:
            y = True
    return y

def move_check_pour(L,direction):
    """
    vérifie s'il reste des animaux favorisant le mouvement dans la liste
    """
    y = False
    for p in L:
        if type(p)!=pion.Rocher and p.orientation==direction:
            y = True
    return y

def move_check_rocher(L):
    """
    vérifie s'il reste des rochers
    """
    y = False
    for p in L:
        if type(p)==pion.Rocher:
            y = True
    return y


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
            Lraw = self[ x , 0:y+1][::-1].copy()

        elif direction == 180:
            Lraw = self[ x:size[0]+1 , y ].copy()

        elif direction == 90:
            Lraw = self[ x, y:size[1]+1 ].copy()

        elif direction == 0:
            Lraw = self[ 0:x+1 , y][::-1].copy()

        Lraw=np.array(Lraw)
        new_L, y = self.move_check(Lraw, direction)

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

    def move_check(self,Lraw,direction):
        """
        à partir de la liste créée par move(), regarde si le mouvement demandé est possible
        """
        possible = True

        L = move_check_delete_none(Lraw).copy()            # on ne garde que les animaux susceptibles de bouger
        L_a_bouger = L.copy()

        while move_check_contre(L,direction) == True:     # tant qu'il reste des animaux s'opposant au mouvement, on cherche à les compenser avec des animaux favorisant le mouvement
            if move_check_pour(L,direction) == False:     # s'il n'y en a plus, le mouvement n'est pas possible
                possible = False
            else:
                pos = -1
                for i in range(len(L)):
                    pi = L[i]
                    if type(pi)!=pion.Rocher and pi.orientation==direction:     # l'animal favorisant qui doit être enlevé pour compenser l'opposant doit être le plus proche de l'opposant
                        pos = i
                    elif type(pi)!=pion.Rocher and pi.orientation==(direction + 180) % 360:
                        L=np.delete(L,i)          # on supprime d'abord L[i] pour ne pas modifer l'indice de L[pos]
                        L=np.delete(L,pos)
                        break
        # il ne peut rester désormais que des animaux favorisants et neutres, et des rochers

        if move_check_pour(L,direction) == False:         # s'il ne reste que des animaux neutres et des rochers, le mouvement n'est pas possible
            possible = False

        while move_check_rocher(L) == True:     # même démarche qu'avec les animaux opposants
            if move_check_pour(L,direction) == False:
                possible = False
            else:
                pos = -1
                for i in range(len(L)):
                    pi = L[i]
                    if type(pi)!=pion.Rocher and pi.orientation==direction:     # l'animal favorisant qui doit être enlevé pour compenser le rocher doit être le plus proche du rocher
                        pos = i
                    elif type(pi)==pion.Rocher:
                        L=np.delete(L,i)          # on supprime d'abord L[i] pour ne pas modifer l'indice de L[pos]
                        L=np.delete(L,pos)
                        break
        # si on est arrivé jusqu'ici sans modifier <possible>, c'est que le mouvement est possible

        return L_a_bouger, possible


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

        else:
            L2 = self[:,x][::-1].copy()
            y=x
            x=4

        L3 = np.array(L2)
        L4 = np.insert(L3,0,[pion.Rhino(0,0,direction)])       # on rajoute un animal dans le sens de la marche pour que move_check() fonctionne
        new_L4, check = self.move_check(L4, direction)

        if tour_elep == True:
            p = pion.Elephant(x,y,direction)
        else:
            p = pion.Rhino(x,y,direction)

        if check:
            for pion_bouge in new_L4[1:]:            # mais on ne bouge pas l'animal rajouté
                pion_bouge.move(direction)
            self.set_pion(p)
            self.update()


        return check, new_L4, p


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
    a.set_pion(pion.Rocher(0,1))
    a.set_pion(pion.Rhino(0,2,90))
    a.set_pion(pion.Rhino(0,3,270))
    print(a)
