import unittest
import numpy as np
from bonbon import *
from grille import *




class Test_Bonbon(unittest.TestCase):
    def test_coord(self):
        grille = Grille(5,5)
        b1= Bonbon1(1,2,grille)
        grille.grille[2][1]=b1
        self.assertEqual(b1.x,1)
        self.assertEqual(b1.y,2)
        self.assertEqual(b1.coords(),(1,2))
        self.assertEqual(b1,grille.grille[2][1])
        



class Test_grille(unittest.TestCase):
    def __init__(self):
        self.grille=Grille(5,5)
        self.grille.remplir()
    def test_var(self):
        grille = Grille(5,5)
        self.assertEqual(grille.dimension,(5,5))
        self.assertEqual(grille.score, 0)
    def test_type(self):
        grille = Grille(5,5)
        self.assertIsInstance(grille,Grille)
    def test_bouger(self):
        b1=Bonbon1(1,0,self.grille)
        b2=Bonbon1(2,0,self.grille)
        b3=Bonbon2(3,0,self.grille) 
        b4=Bonbon1(4,0,self.grille)
        self.grille.grille[0][1],self.grille.grille[0][2],self.grille.grille[0][3],self.grille.grille[0][4]=b1,b2,b3,b4
        self.grille.bouger(b3,b4)
        assertEqual(b3,grille.grille[0][4])
        
        
        

if __name__ == '__main__':
    unittest.main()

    