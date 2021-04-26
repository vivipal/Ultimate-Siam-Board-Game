import pion
import board

ingame = True
tour_elep = True

plateau = board.Board((5,5),dtype=object)     # initialisation
plateau.set_pion(pion.Rocher(2,1))
plateau.set_pion(pion.Rocher(2,2))
plateau.set_pion(pion.Rocher(2,3))
print(plateau)

def choice():
    choice = check_choice()

    if choice==1:
        x,y,p = check_piece()
        choice_turn(x,y,p)

    elif choice==2:
        x,y,p = check_piece()
        choice_move(p)


def choice_turn(x,y,p):
    new_direction = check_direction(x,y,p)

    if tour_elep == True:
        a_placer = pion.Elephant(x,y,new_direction)
    else:
        a_placer = pion.Rhino(x,y,new_direction)

    plateau.set_pion(a_placer)

def choice_move(p):
    dir = check_direction()
    L_moved, y = plateau.move(p,dir)

    if y == False:
        print("Impossible to push, try again")
        choice()






def check_piece():
    cmd = input("What piece ? xy")

    if cmd == "esc":
        choice()

    try:
        x=cmd[0]
        y=cmd[1]
        p = plateau[x,y]
    except:
        print("Incorrect input, try again")
        check_piece()

    if p == None:
        print("Empty, try again")
        check_piece()
    elif type(p) == pion.Rocher:
        print("It's a rock, try again")
        check_piece()
    elif (type(p) == pion.Rhino and tour_elep == True) or (type(p) == pion.Elephant and tour_elep == False):
        print("Not your animal, try again")
        check_piece()
    else:
        return(x,y,p)

def check_direction():
        cmd = input("In which direction ? 0,90,180,270")

        try:
            new_direction = int(cmd2)
        except:
            print("Not an integer, try again")
            check_direction()

        if not (new_direction==0 or new_direction==90 or new_direction==180 or new_direction==270):
            print("Incorrect input, try again")
            check_direction()

        return new_direction

def check_choice():
    cmd = input("What do you want to do ? \n turn a piece in place 1 \n move piece 2 \n add a new piece 3")

    try:
        choice = int(cmd)
    except:
        print("Not an integer, try again")
        check_choice()

    if not (choice==1 or choice==2 or choice==3):
        print("Incorrect input, try again")
        check_choice()

    return choice



# while ingame:
#     j_rhino = not j_rhino
#     print(plateau)
