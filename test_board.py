import unittest

from board import Board
import pion
from numpy import ndarray,array


class TestBoard(unittest.TestCase):

    def setUp(self):

        self.board = Board((5,5),dtype=object)

        self.board[1,1] = pion.Rhino(1,1,90)
        self.board[3,1] = pion.Rhino(3,1,90)
        self.board[3,3] = pion.Rhino(3,3,90)
        self.board[2,4] = pion.Elephant(2,4,90)



    def testInit(self):
        """
        Test de la méthode d’initialisation
        """

        # variables bien initialisées
        self.assertEqual(self.board.tour_elephant,True)
        self.assertEqual(self.board.nb_tour,0)

        # on regarde si on a bien 3 rochers au millieu
        self.assertEqual(type(self.board[2,1]), pion.Rocher)
        self.assertEqual(type(self.board[2,2]), pion.Rocher)
        self.assertEqual(type(self.board[2,3]), pion.Rocher)


    def testArray(self):
        """
        Test si un rhinocéros est bien un animal
        """

        self.assertIsInstance(self.board, ndarray)


    def testNbRocher(self):
        """
        Test le nomre de rochers
        """

        self.assertEqual(self.board.nb_rocher(),3)

    def testNbRhino(self):
        """
        Test le nomre de rhinocéros
        """
        self.assertEqual(self.board.nb_rhino(),3)

    def testNbElephant(self):
        """
        Test le nomre d'éléphants
        """
        self.assertEqual(self.board.nb_elephant(),1)


    def testNbMaxInsert(self):
        """
        Test si on ne peut pas ajouter plus de 5 piece par joueur
        """

        b = Board((5,5),dtype=object)

        # pour les elephants :
        b[1,1] = pion.Elephant(1,1,90)
        b[3,1] = pion.Elephant(3,1,90)
        b[3,3] = pion.Elephant(3,3,90)
        b[2,4] = pion.Elephant(2,4,90)
        b[1,4] = pion.Elephant(1,4,90)

        self.assertEqual(b.check_insert(),0)

        # pour les rhino :
        b.tour_elephant = False
        b[1,1] = pion.Rhino(1,1,90)
        b[3,1] = pion.Rhino(3,1,90)
        b[3,3] = pion.Rhino(3,3,90)
        b[2,4] = pion.Rhino(2,4,90)
        b[1,4] = pion.Rhino(1,4,90)

        self.assertEqual(b.check_insert(),0)


    def testUpdateBoard(self):
        """
        Test si après avoir bouger les pions, après l'appel à Board.update,
        les pions doivents etre bien placé dans la Board
        """

        b = Board((5,5),dtype=object)

        # on fait exprès de mal placer les pions dans b
        b[3,1] = pion.Elephant(1,1,90)
        b[3,3] = pion.Elephant(3,1,270)
        b[1,4] = pion.Rhino(3,3,90)
        b[1,1] = pion.Rhino(2,4,0)
        b[2,4] = pion.Elephant(1,4,180)

        # normalement les pions sont bien replacé
        b.update()

        x_lim,y_lim = b.shape

        for i in range(x_lim) :
            for j in range(y_lim) :
                if b[i,j] != None:
                    self.assertEqual(b[i,j].coords, (i,j))


    def testMoveCheck(self):
        """
        Test si un mouvement est possible
        """

        # 1 contre 1 --> impossible
        pion1 = pion.Rhino(0,1,180)
        pion2 = pion.Elephant(0,2,0)
        ligne_1 = array([pion1,pion2])

        # 2 contre 1 --> possible
        pion1 = pion.Rhino(0,1,180)
        pion3 = pion.Rhino(0,2,180)
        pion2 = pion.Elephant(0,3,0)
        ligne_2 = array([pion1,pion2,pion3])

        # exemple complexe --> possible
        pion1 = pion.Rhino(0,1,180)
        pion2 = pion.Elephant(0,2,90)
        pion3 = pion.Elephant(0,3,180)
        pion4 = pion.Rocher(0,4)
        pion5 = pion.Rhino(0,5,0)
        ligne_3 = array([pion1,pion2,pion3,pion4,pion5])

        # exemple complexe --> impossible
        pion1 = pion.Rhino(0,0,180)
        pion2 = pion.Rocher(0,1)
        pion3 = pion.Elephant(0,2,90)
        pion4 = pion.Elephant(0,3,180)
        pion5 = pion.Rocher(0,4)
        pion6 = pion.Rhino(0,5,0)
        ligne_4 = array([pion1,pion2,pion3,pion4,pion5,pion6])

        # 1 contre 2 mal orienté --> possible
        pion1 = pion.Rhino(0,1,180)
        pion3 = pion.Elephant(0,2,90)
        pion2 = pion.Elephant(0,3,270)
        ligne_5 = array([pion1,pion2,pion3])


        self.assertEqual(self.board.move_check(ligne_1,180)[1],0)
        self.assertEqual(self.board.move_check(ligne_2,180)[1],1)
        self.assertEqual(self.board.move_check(ligne_3,180)[1],1)
        self.assertEqual(self.board.move_check(ligne_4,180)[1],0)
        self.assertEqual(self.board.move_check(ligne_5,180)[1],1)


if __name__ == '__main__':
    unittest.main()
