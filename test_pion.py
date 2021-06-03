import unittest

from pion import Rocher, Rhino


class TestRhino(unittest.TestCase):

    def setUp(self):
        pass

    def testInit(self):
        """
        Test de la méthode d’initialisation
        """
        rhino = Rhino(2,3,180)

        self.assertEqual(rhino.x,2)
        self.assertEqual(rhino.y,3)
        self.assertEqual(rhino.orientation,180)
        self.assertEqual(rhino.espece,'R')



    def testInitWrongPosition(self):
        """
        Test de l'initialisation d'une pièce avec des coordonnées négatives
        """

        with self.assertRaises(Exception):
            a=Rhino(2,-2,0)
            b=Rhino(-3,-1,0)
            c=Rhino(-1,4,0)

    def testInitWrongPosition(self):
        """
        Test de l'initialisation d'une pièce avec une orientation impossible
        """

        with self.assertRaises(Exception):
            a=Rhino(2,-2,80)



    def testMove(self):
        """
        Test du mouvement d'une pièce
        """

        r = Rhino(1,2,90)
        r.move(180)

        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)


if __name__ == '__main__' :
    unittest.main()
