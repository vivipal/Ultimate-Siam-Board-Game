import pion
import board


def choice():
    print(plateau)
    choice = check_choice()

    if choice==1:
        x,y,p = check_piece()
        choice_turn(x,y,p)

    elif choice==2:
        x,y,p = check_piece()
        choice_move(x,y,p)

    elif choice==3:
        dir, x = check_insert()
        choice_insert(tour_elep,dir,x)


def choice_turn(x,y,p):
    new_direction = check_direction()
    p.turn(new_direction)

def choice_move(x,y,p):
    dir = check_direction()
    L_moved, y, W = plateau.move(p,dir)

    if len(W)==1:
        victory(W[0])

    elif y == False:
        print("Impossible to push, try again \n")
        choice()

    elif len(L_moved) <= 1:
        print("Enter final direction \n")
        choice_turn(x,y,p)

def choice_insert(tour_elep,dir,x):
    check, L_moved, p = plateau.insert(tour_elep,dir,x)
    xp,yp = p.coords
    if check == False:
        print("Impossible to insert, try again \n")
        choice()
    elif len(L_moved) <= 1:
        print("Enter final direction \n")
        choice_turn(xp,yp,p)


def victory(espece):
    str = "Elephants"*tour_elep + "Rhinoceros"*(not tour_elep)
    print("Les "+str+"ont gagné !")
    print("")
    print("--------------- FIN --------------------")
    print("")


def check_choice():
    cmd = input("What do you want to do ? \n turn a piece in place 1 \n move piece 2 \n add a new piece 3 \n")

    try:
        choice = int(cmd)
    except:
        print("Not an integer, try again \n")
        check_choice()

    if not (choice==1 or choice==2 or choice==3):
        print("Incorrect input, try again \n")
        check_choice()

    return choice

def check_piece():
    cmd = input("What piece ? xy \n")

    try:
        x = int(cmd[0])
        y = int(cmd[1])
        p = plateau[x,y]
    except:
        print("Incorrect input, try again \n")
        check_choice()

    if p == None:
        print("Empty, try again \n")
        check_choice()
    elif type(p) == pion.Rocher:
        print("It's a rock, try again \n")
        check_choice()
    elif (type(p) == pion.Rhino and tour_elep == True) or (type(p) == pion.Elephant and tour_elep == False):
        print("Not your animal, try again \n")
        check_choice()
    else:
        return(x,y,p)

def check_direction():
        cmd = input("In which direction ? 0,90,180,270 \n")

        try:
            new_direction = int(cmd)
        except:
            print("Not an integer, try again \n")
            check_direction()

        if not (new_direction==0 or new_direction==90 or new_direction==180 or new_direction==270):
            print("Incorrect input, try again \n")
            check_direction()

        return new_direction

def check_insert():
    nb_e, nb_rh, nb_ro = plateau.nb_elephant, plateau.nb_rhino, plateau.nb_rocher
    if (nb_e==5 and tour_elep==True) or (nb_rh==5 and tour_elep==False):
        print("You can't have more than 5 pieces, try again")
        choice()

    dir = check_direction()

    cmd = input("At which position ? \n")

    try:
        x = int(cmd)
    except:
        print("Not an integer, try again \n")
        check_insert()

    if (dir==0 or dir==180) and x==2:
        print("Impossible to place here, try again \n")
        check_insert()
    elif not 0<=x<4:
        print("Incorrect input, try again \n")
        check_insert()

    return dir,x

if __name__=='__main__' :
    ingame = True
    tour_elep = True

    plateau = board.Board((5,5),dtype=object)
    plateau.set_pion(pion.Elephant(0,0,90))
    plateau.set_pion(pion.Rocher(0,1))
    plateau.set_pion(pion.Elephant(0,2,90))
    plateau.set_pion(pion.Elephant(0,3,270))
    plateau.set_pion(pion.Elephant(0,4,0))

    while ingame:
        print("--------------------------")
        str = "Elephants"*tour_elep + "Rhinoceros"*(not tour_elep)
        print("Au tour des "+str+"\n")
        choice()
        tour_elep = not tour_elep
