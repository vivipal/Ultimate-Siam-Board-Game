import pion
import board

ingame = True
j_elep = True

plateau = Board((5,5),dtype=object)     # initialisation
plateau.set_pion(pion.Rocher(2,1))
plateau.set_pion(pion.Rocher(2,2))
plateau.set_pion(pion.Rocher(2,3))
print("plateau)

def choice():
    cmd = input("What do you want to do ? \n turn a piece "1" \n move and turn a piece "2" \n push pieces "3"")

    if cmd == "1":
        try :
            choice_1_coords
        except:
            print()

    elif cmd == "2":
        sdsds
    else:
        dsds

def choice_1_coords():
    cmd = input(What piece do you want to move ? "xy")
    x=cmd[0]
    y=cmd[1]

    if x<0 or x>4 or y<0 or y>4:
        print("Out of bounds, try again")
        choice_1_coords()
    elif plateau[x,y] == None:
        print("Empty, try again")
        choice_1_coords()
    elif (type(plateau[x,y]) == pion.Rhino and j_elep == True) or (type(plateau[x,y]) == pion.Elephant and j_elep == False):
        print("Not your animal, try again")
        choice_1_coords()
    else:
        

while ingame:
    j_rhino = not j_rhino
    print(plateau)
