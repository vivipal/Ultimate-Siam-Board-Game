import numpy as np

class Board(np.ndarray): 

    def __new__(self,size):
        """
        size tuple represent the size of the board game.
        """

        super().__init__(size, dtype=object)

test = Board((5,5))
print(test)

#print(np.ndarray((5,5), dtype=object))
