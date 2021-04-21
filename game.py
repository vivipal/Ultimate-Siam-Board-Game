import pion
import board

ingame = True

plateau = Board((5,5),dtype=object)     # initialisation
plateau.set_pion(pion.Rocher(2,1))
plateau.set_pion(pion.Rocher(2,2))
plateau.set_pion(pion.Rocher(2,3))
print("plateau)

while ingame:
