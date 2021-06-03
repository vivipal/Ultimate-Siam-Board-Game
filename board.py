import numpy as np
import pion


class Board(np.ndarray):
    '''
    Classe représentant le plateau de jeu
    '''

    def __init__(self,size=(5,5),dtype=object):
        """
        le tuple size represente la taille du plateau
        """
        self.tour_elephant = True       # les éléphants commencent toujours
        self.nb_tour = 0

        self[2,1]=pion.Rocher(2,1)      # on place les 3 rochers au centre du plateau
        self[2,2]=pion.Rocher(2,2)
        self[2,3]=pion.Rocher(2,3)

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
        compte le nombre de rhinocéros
        """
        nb = 0
        for p in self.ravel():
            if type(p) == pion.Rhino:
                nb += 1
        return nb

    def nb_elephant(self):
        """
        compte le nombre d'éléphants
        """
        nb = 0
        for p in self.ravel():
            if type(p) == pion.Elephant:
                nb += 1
        return nb

    def nb_rocher(self):
        """
        compte le nombre de rochers
        """
        nb = 0
        for p in self.ravel():
            if type(p) == pion.Rocher:
                nb += 1
        return nb

    def check_insert(self):
        """
        Permet de savoir si le joueur en cours peut encore ajouter une pièce sur le plateau
        """
        if self.tour_elephant and self.nb_elephant()>=5 :      # chaque joueur a 5 pions
            return 0
        elif not self.tour_elephant and self.nb_rhino()>=5 :
            return 0
        else :
            return 1

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

    def new_board(self):
        """
        réinitialise le plateau et place des rochers au milieu
        """
        self.clear()

        self[2,1]=pion.Rocher(2,1)
        self[2,2]=pion.Rocher(2,2)
        self[2,3]=pion.Rocher(2,3)

    def update(self):
        """
        met à jour Board selon les nouvelles coordonnées des pions
        """
        copy = self.copy()          # on copie les pions sur le plateau dont les coords ont été mises à jour
        self.clear()                # on vide le plateau
        for p in copy.ravel():
            if p != None and 0<=p.x<=4 and 0<=p.y<=4:       # on remet les pions selon leurs nouvelles coords
                self[p.x, p.y] = p

    def next_turn(self):
        self.tour_elephant = not self.tour_elephant
        self.nb_tour += 1

    def move_check(self,Lraw,direction):
        """
        à partir de la liste créée par move(), regarde si le mouvement demandé est possible
        """
        possible = True

        L = self.move_check_delete_none(Lraw).copy()            # on ne garde que les animaux susceptibles de bouger
        L_a_bouger = L.copy()

        if len(L)==1:
            pass

        else:
            while self.move_check_contre(L,direction) == True:     # tant qu'il reste des animaux s'opposant au mouvement, on cherche à les compenser avec des animaux favorisant le mouvement
                if self.move_check_pour(L,direction) == False:     # s'il n'y en a plus, le mouvement n'est pas possible
                    possible = False
                    break
                else:
                    for i in range(len(L)):
                        pi = L[i]
                        if type(pi)!=pion.Rocher and pi.orientation==direction:     # l'animal favorisant qui doit être enlevé pour compenser l'opposant doit être le plus proche de l'opposant
                            pos = i
                        elif type(pi)!=pion.Rocher and pi.orientation==(direction + 180) % 360:
                            L=np.delete(L,i)          # on supprime d'abord L[i] pour ne pas modifer l'indice de L[pos]
                            L=np.delete(L,pos)
                            break
            # il ne peut rester désormais que des animaux favorisants et neutres, et des rochers

            if self.move_check_pour(L,direction) == False:         # s'il ne reste que des animaux neutres et des rochers, le mouvement n'est pas possible
                possible = False

            while self.move_check_rocher(L) == True:     # même démarche qu'avec les animaux opposants
                if self.move_check_pour(L,direction) == False:
                    possible = False
                    break
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

    def move(self,animal,direction):
        """
        fait bouger le pion dans la direction demandée, pousse les pions devant si possible
        """
        x = animal.x
        y = animal.y
        size = np.shape(self)

        # on récupère le contenu des cases en face du pion souhaitant bouger
        if direction == 270:
            Lraw = self[ x , 0:y+1][::-1].copy()

        elif direction == 180:
            Lraw = self[ x:size[0]+1 , y ].copy()

        elif direction == 90:
            Lraw = self[ x, y:size[1]+1 ].copy()

        elif direction == 0:
            Lraw = self[ 0:x+1 , y][::-1].copy()

        Lraw=np.array(Lraw)
        new_L, y = self.move_check(Lraw, direction)     # selon ce qu'il y a devant le pion souhaitant bouger, le mouvement sera possible ou non
        W = ''                              # stockera le nom de l'équipe gagnante si la partie se termine

        if y:                               # si le mouvement est possible
            for pion_bouge in new_L:        # on fait bouger tous les pions se trouvant devant celui souhaitant bouger
                pion_bouge.move(direction)
                if type(pion_bouge)==pion.Rocher and not (0>pion_bouge.x>4 and 0>pion_bouge.y>4):       # si un rocher est sorti (partie terminée)
                    for pion_win in new_L:                                                              # on détermine l'équipe gagnante
                        if type(pion_win)!=pion.Rocher and pion_win.orientation == direction:
                            W = [pion_win]

        self.update()

        return new_L, y, W

    def insert(self,direction,x):
        """
        renvoie la nouvelle position ou None si l'insertion est impossible
        """
        # de la même façon que move()
        if direction == 270:
            L = self[x,:][::-1].copy()
            y=4

        elif direction == 180:
            L = self[:,x].copy()
            y=x
            x=0

        elif direction == 90:
            L = self[x,:].copy()
            y=0

        else:
            L = self[:,x][::-1].copy()
            y=x
            x=4

        if self.tour_elephant == True:          # selon le tour, on insèrera un éléphant ou un rhinocéros
            p = pion.Elephant(x,y,direction)
        else:
            p = pion.Rhino(x,y,direction)

        L = np.array(L)
        L = np.insert(L,0,p)                    # le pion à insérer peut pousser devant lui, il est donc ajouté à la liste pour move_check()
        new_L, check = self.move_check(L, direction)

        if check:                               # si l'insertion est possible on pousse les pions concernés
            for pion_bouge in new_L[1:]:        # mais on ne bouge pas l'animal à insérer
                pion_bouge.move(direction)
            self.update()
            self.set_pion(p)                    # on insère l'animal à insérer
            self.update()
            return p.x,p.y

        else :
            return None

    def move_check_delete_none(self,L):
        """
        transforme la liste créée par move() en ne gardant que les pions susceptibles de bouger (du pion à bouger jusqu'à la prochaine case vide)
        """
        L_return = []
        for l in L:
            if l!=None:
                L_return.append(l)
            else:
                break
        L_return = np.array(L_return)
        return L_return

    def move_check_contre(self,L,direction):
        """
        vérifie s'il reste des animaux s'opposant au mouvement dans la liste L
        """
        y = False
        for p in L:
            if type(p)!=pion.Rocher and p.orientation==(direction + 180) % 360:
                y = True
                break
        return y

    def move_check_pour(self,L,direction):
        """
        vérifie s'il reste des animaux favorisant le mouvement dans la liste L
        """
        y = False
        for p in L:
            if type(p)!=pion.Rocher and p.orientation==direction:
                y = True
                break
        return y

    def move_check_rocher(self,L):
        """
        vérifie s'il reste des rochers dans la liste L
        """
        y = False
        for p in L:
            if type(p)==pion.Rocher:
                y = True
                break
        return y

    def verify_piece(self,piece):
        """
        vérifie si le tour de jeu correspond au pion piece
        """
        if self.tour_elephant == True and type(piece)==pion.Elephant :
            return 1
        elif self.tour_elephant == False and type(piece)==pion.Rhino :
            return 1
        else : return 0
