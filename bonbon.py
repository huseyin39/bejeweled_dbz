#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:40:05 2017


@author: kizil-khalile
"""
from grille import *
import numpy as np
from PyQt4 import QtGui, QtCore

class Bonbon():
    def __init__(self,x,y,grille):
        self.x=x
        self.y=y
        self._grille=grille.grille
        
    def __str__(self):
        return "{}".format(self.car())
    
    def coords(self):
        return (self.x, self.y)    
    
    def test_alignement_gauche(self,x2,y2):
        """Ceci est une fonction qui teste la possibilité pour un bonbon
        donné d'effectuer un déplacement vers la gauche et renvoie une
        liste comprenant les bonbons à supprimer (peut être vide)"""

        n=self._grille.shape[0]  #nombre de lignes
        m=self._grille.shape[1]  #nombre de colonnes
        x,y=self.x,self.y
        Res=[]
        l=""
        if x2>1: # Test s'il y a 2 bonbons à sa gauche
            if self.car()==self._grille[y2][x2-1].car()==self._grille[y2][x2-2].car():
                Res.append(self)
                Res.append(self._grille[y2,x2-1])
                Res.append(self._grille[y2,x2-2])
                l="Hr"
        if y2>1 : #Test s'il y a 2 bonbons au dessus
            if self.car()==self._grille[y2-1][x2].car()==self._grille[y2-2][x2].car():
                Res.append(self)
                Res.append(self._grille[y2-1,x2])
                Res.append(self._grille[y2-2,x2])
                l="Vr"
        if y2<n-2: #Test s'il y a 2 bonbons au dessous
            if self.car()==self._grille[y2+1][x2].car()==self._grille[y2+2][x2].car():
                Res.append(self)
                Res.append(self._grille[y2+1][x2])
                Res.append(self._grille[y2+2][x2])
                l="Vr"
        if (y2<n-1 and y2>0): #Test si on est entre 2 bonbons (Vertical)
            if self.car()==self._grille[y2-1][x2].car()==self._grille[y2+1][x2].car():
                Res.append(self)
                Res.append(self._grille[y2-1][x2])
                Res.append(self._grille[y2+1][x2])
                l="Vr"
        return list(set(Res)),l #Supprime les doublons
        

    def test_alignement_droite(self,x2,y2):
        """Ceci est une fonction qui teste la possibilité pour un bonbon
        donné d'effectuer un déplacement vers la droite et renvoie une
        liste comprenant les bonbons à supprimer (peut être vide)"""
        n=self._grille.shape[0]  #nombre de lignes
        m=self._grille.shape[1]  #nombre de colonnes
        x,y=self.x,self.y
        Res=[]
        l=""
        if x2<m-2: # Test s'il y a 2 bonbons à sa droite
            if self.car()==self._grille[y2][x2+1].car()==self._grille[y2][x2+2].car():
                Res.append(self)
                Res.append(self._grille[y2,x2+1])
                Res.append(self._grille[y2,x2+2])
                l="Hr"
        if y2>1 : #Test s'il y a 2 bonbons au dessus
            if self.car()==self._grille[y2-1][x2].car()==self._grille[y2-2][x2].car():
                Res.append(self)
                Res.append(self._grille[y2-1,x2])
                Res.append(self._grille[y2-2,x2])
                l="vr"
        if y2<n-2: #Test s'il y a 2 bonbons au dessous
            if self.car()==self._grille[y2+1][x2].car()==self._grille[y2+2][x2].car():
                Res.append(self)
                Res.append(self._grille[y2+1][x2])
                Res.append(self._grille[y2+2][x2])
                l="Vr"
        if (y2<n-1 and y2>0): #Test si on est entre 2 bonbons (Vertical)
            if self.car()==self._grille[y2-1][x2].car()==self._grille[y2+1][x2].car():
                Res.append(self)
                Res.append(self._grille[y2-1][x2])
                Res.append(self._grille[y2+1][x2])
                l="Vr"
        return list(set(Res)),l #Supprime les doublons
            
        
    def test_alignement_haut(self,x2,y2):
        """Ceci est une fonction qui teste la possibilité pour un bonbon
        donné d'effectuer un déplacement vers le haut et renvoie une
        liste comprenant les bonbons à supprimer (peut être vide)"""        
        n=self._grille.shape[0]  #nombre de lignes
        m=self._grille.shape[1]  #nombre de colonnes
        x,y=self.x,self.y
        Res=[]
        l="Hr"
        if y2>1 : #Test s'il y a 2 bonbons au dessus
            if self.car()==self._grille[y2-1][x2].car()==self._grille[y2-2][x2].car():
                Res.append(self)
                Res.append(self._grille[y2-1][x2])
                Res.append(self._grille[y2-2][x2])
                l="Vr"
        if x2>1: # Test s'il y a 2 bonbons à sa gauche
            if self.car()==self._grille[y2][x2-1].car()==self._grille[y2][x2-2].car():
                Res.append(self)
                Res.append(self._grille[y2][x2-1])
                Res.append(self._grille[y2][x2-2])
                l="Hr"
        if x2<m-2: #Test s'il y a 2 bonbons à sa droite
            if self.car()==self._grille[y2][x2+1].car()==self._grille[y2][x2+2].car():
                Res.append(self)
                Res.append(self._grille[y2][x2+1])
                Res.append(self._grille[y2][x2+2])
                l="Hr"
        if (x2<m-1 and x2>0): #Test si on est entre 2 bonbons (Horizontal)
            if self.car()==self._grille[y2][x2+1].car()==self._grille[y2][x2-1].car():
                Res.append(self)
                Res.append(self._grille[y2][x2+1])
                Res.append(self._grille[y2][x2-1])
                l="Hr"
        return list(set(Res)),l #Supprime les doublons
        
    def test_alignement_bas(self,x2,y2):
        """Ceci est une fonction qui teste la possibilité pour un bonbon
        donné d'effectuer un déplacement vers le bas et renvoie une
        liste comprenant les bonbons à supprimer (peut être vide)"""
        n=self._grille.shape[0]  #nombre de lignes
        m=self._grille.shape[1]  #nombre de colonnes
        Res=[]
        x,y=self.x,self.y
        l="Hr"
        if y2<n-2: #Test s'il y a 2 bonbons au dessous
            if self.car()==self._grille[y2+1][x2].car()==self._grille[y2+2][x2].car():
                Res.append(self)
                Res.append(self._grille[y2+1][x2])
                Res.append(self._grille[y2+2][x2])
                l="Vr"
        if x2>1: # Test s'il y a 2 bonbons à sa gauche
            if self.car()==self._grille[y2][x2-1].car()==self._grille[y2][x2-2].car():
                Res.append(self)
                Res.append(self._grille[y2][x2-1])
                Res.append(self._grille[y2][x2-2])
                l="Hr"
        if x2<m-2: #Test s'il y a 2 bonbons à sa droite
            if self.car()==self._grille[y2][x2+1].car()==self._grille[y2][x2+2].car():
                Res.append(self)
                Res.append(self._grille[y2][x2+1])
                Res.append(self._grille[y2][x2+2])
                l="Hr"
        if (x2<m-1 and x2>0): #Test si on est entre 2 bonbons (Horizontal)
            if self.car()==self._grille[y2][x2+1].car()==self._grille[y2][x2-1].car():
                Res.append(self)
                Res.append(self._grille[y2][x2+1])
                Res.append(self._grille[y2][x2-1])
                l="Hr"
        return list(set(Res)),l #Supprime les doublons     
      
    def car(self):
       pass
    
        
class Bonbon1(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon1"
        
class Bonbon2(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon2"
        

class Bonbon3(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon3"
        

class Bonbon4(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon4"

        
class Bonbon5(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon5"
        

class Bonbon6(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon6"

class Bonbon7(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon7"

        
class BonbonNoir(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon Noir"
        
class BonbonSuper(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon SUPER"  

class BonbonGenial(Bonbon):
    def __init__(self, x,y,grille):
        super().__init__(x, y, grille)
    
    def car(self):
        return "Bonbon Genial"        
        