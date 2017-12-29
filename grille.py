#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:38:06 2017

@author: kizilhu
"""
import numpy as np
from bonbon import *
from numpy.random import randint
import random
from candy import Ui_MainWindow

class Grille():
    def __init__(self,n,m,nive=1):
        self.__n=n
        self.__m=m
        self.grille=np.zeros([n,m],dtype=object)
        self.score=0
        self.aides_restantes=1
        self.niveau=nive
        self.niv_dic={1:60,
                      2:55,
                      3:50,
                      4:45,
                      5:40,
                      6:35,
                      7:30,
                      8:"Fini"
                      }
    def __str__(self):
        print(self.grille)
        
    def bouger(self,bonbon,ptarr):
        """ Cette fonction teste si le mouvement sélectionné est autorisé,
        s'il l'est alors le mouvement est effectué.
        ptarr = objet avec lequel self doit échanger de position"""
        if bonbon.car()!='Bonbon Noir' and ptarr.car()!='Bonbon Noir':
            x1, x2 =bonbon.x, ptarr.x
            y1, y2 = bonbon.y, ptarr.y
            differencex=x2-x1
            differencey=y2-y1
            if ptarr==bonbon and bonbon.car()=="Bonbon Genial":
                self.explose(self.liste_explosesuper(bonbon))
                
            else:
                if differencex==1 and differencey==0: #Déplacement à droite
                    l1_explose,l1=(bonbon.test_alignement_droite(x2,y2))
                    l2_explose,l2=(ptarr.test_alignement_gauche(x1,y1))
                    liste_bonbons_exploses= l1_explose+l2_explose
                    S1= self.newliste_explose(self.Superoupas(l1_explose,l1,x2,y2))
                    S2= self.newliste_explose(self.Superoupas(l2_explose,l2,x1,y1))
                    n1= len(l1_explose)
                    n2= len(l2_explose)
                    if n1==5 or n2==5:
                        if n1==n2==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses)) 
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        elif n1==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))  
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        else: 
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)                             
                    elif n1==4 or n2==4:
                        if n1==4 and n2==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                            
                        elif n1==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                        
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                        
                        else :
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            
                    else:
                        if (S1+S2) != []:
                            self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                        elif liste_bonbons_exploses!=[]:
                            self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                        
                        
                elif differencex==-1 and differencey==0: #Déplacement à gauche
                    l1_explose,l1=(bonbon.test_alignement_gauche(x2,y2))
                    l2_explose,l2=(ptarr.test_alignement_droite(x1,y1))
                    liste_bonbons_exploses= l1_explose+l2_explose
                    S1= self.newliste_explose(self.Superoupas(l1_explose,l1,x2,y2))
                    S2= self.newliste_explose(self.Superoupas(l2_explose,l2,x1,y1))
                    n1= len(l1_explose)
                    n2= len(l2_explose)
                    if n1==5 or n2==5:
                        if n1==n2==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses)) 
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        elif n1==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))  
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        else: 
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)  
                    elif n1==4 or n2==4:
                        if n1==4 and n2==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                            
                        elif n1==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                        
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                        
                        else :
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            
                    else:
                        if (S1+S2) != []:
                            self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                        elif liste_bonbons_exploses!=[]:
                            self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                elif differencey==1 and differencex==0: #Déplacement en bas
                    l1_explose,l1=(bonbon.test_alignement_bas(x2,y2))
                    l2_explose,l2=(ptarr.test_alignement_haut(x1,y1))
                    liste_bonbons_exploses= l1_explose+l2_explose
                    S1= self.newliste_explose(self.Superoupas(l1_explose,l1,x2,y2))
                    S2= self.newliste_explose(self.Superoupas(l2_explose,l2,x1,y1))
                    n1= len(l1_explose)
                    n2= len(l2_explose)
                    if n1==5 or n2==5:
                        if n1==n2 and  n1==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses)) 
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        elif n1==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))  
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        else: 
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)  
                    elif n1==4 or n2==4:
                        if n1==4 and n2==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                            
                        elif n1==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                        
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                        
                        else :
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            
                    else:
                        if (S1+S2) != []:
                            self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                        elif liste_bonbons_exploses!=[]:
                            self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                        
                elif differencey==-1 and differencex==0: # Déplacement à droite
                    l1_explose,l1=(bonbon.test_alignement_haut(x2,y2))
                    l2_explose,l2=(ptarr.test_alignement_bas(x1,y1))
                    liste_bonbons_exploses= l1_explose+l2_explose
                    S1= self.newliste_explose(self.Superoupas(l1_explose,l1,x2,y2))
                    S2= self.newliste_explose(self.Superoupas(l2_explose,l2,x1,y1))
                    n1= len(l1_explose)
                    n2= len(l2_explose)
                    if n1==5 or n2==5:
                        if n1==n2 and n2==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses)) 
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        elif n1==5:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))  
                            self.grille[y2][x2]= BonbonGenial(x2,y2,self)
                        else: 
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            self.grille[y1][x1]= BonbonGenial(x1,y1,self)  
                    elif n1==4 or n2==4:
                        if n1==4 and n2==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                            
                        elif n1==4:
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                        
                            self.grille[y2][x2]= BonbonSuper(x2,y2,self)
                        
                        else :
                            if (S1+S2) != []:
                                self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                            else:    
                                self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                            
                            self.grille[y1][x1]= BonbonSuper(x1,y1,self)
                            
                    else:
                        if (S1+S2) != []:
                            self.explose(self.echange(bonbon,ptarr,(S1+S2)))
                        elif liste_bonbons_exploses!=[]:
                            self.explose(self.echange(bonbon,ptarr,liste_bonbons_exploses))
                        
                else:
                        print ("Les bonbons doivent être adjacents")
        
        
    def explose(self,liste):
        """ Cette fonction permet de d'exploser les bonbons en partant de la liste
        des bonbons qu'il y a à exploser. Pour cela, nous explosons les bonbons
        par y décroissants.""" 
        
        L,L_coords=trier_par_y_decroissant(liste)
        n=len(L)
        for k in range(n):
            self.explose_bis(L.pop())
        L3=[]  #L3 va etre la liste des nouveaux bonbons pour tests alignements
        for i in L_coords:
            for k in range (self.__n-1,-1,-1):
                L3+=self.test_deja_alignement(k,i)
        L3=list(set(L3))
        if L3!=[]:
            self.explose(L3)
                
    def explose_bis(self,bonbon):
        self.score+=1
        """Ils sont remplacés par les bonbons situés au dessus d'eux.
        Les bonbons situés à l'extrémités sont remplacés par les bonbons
        de la grille_annexe."""
        
        x=bonbon.x
        y=bonbon.y
        
        for k in range(y,0,-1):
            if not(self.grille[k][x].car()==self.grille[k-1][x].car()=='Bonbon Noir'):
                if self.grille[k-1][x].car()=='Bonbon Noir':
                    if self.grille[k-2][x].car()=='Bonbon Noir':
                        self.grille[k][x]=self.grille[k-3][x]
                        self.grille[k][x].y=k
                    else: 
                        self.grille[k][x]=self.grille[k-2][x]
                        self.grille[k][x].y=k
                else :
                    if self.grille[k][x].car()!='Bonbon Noir':
                    
                        self.grille[k][x]=self.grille[k-1][x]
                        self.grille[k][x].y=k
        self.grille[0][x]=self.randombonbon(0,x)
        
    @property
    def dimension(self):
        """Cette fonction retourne les dimensions de la grille principale"""
        
        return (self.__n,self.__m)
        
    def remplir(self):
        """Cette méthode remplit en début de chaque partie et de chaque niveau 
        la grille aléatoirement. De plus, nous avons pris en compte le fait 
        qu’il soit possible qu’il y ait des alignements à la génération 
        de la grille. Alors nous les explosons sans les prendre en compte 
        pour le score."""
        
        for i in range(self.dimension[0]):
            for j in range (self.dimension[1]):
                self.grille[i][j]=self.randombonbon(i,j)
        # Cela permet de voir à la création les alignements présents
        liste_bonbons_alignes=[]
        for i in range(self.dimension[0]):
            for j in range (self.dimension[1]):
                liste_bonbons_alignes+=self.test_deja_alignement(i,j)
        liste_bonbons_alignes=list(set(liste_bonbons_alignes))
        self.explose(liste_bonbons_alignes)
        self.aides_restantes=1
        if self.niveau==2:
            self.aides_restantes+=1
            self.grille[2][2]=BonbonNoir(2,2,self)
            self.grille[6][6]=BonbonNoir(6,6,self)
        elif self.niveau==3:
            self.aides_restantes+=2
            self.grille[2][4]=BonbonNoir(2,5,self)
            self.grille[6][1]=BonbonNoir(6,1,self)
            self.grille[6][7]=BonbonNoir(6,7,self)
        elif self.niveau==4:
            self.aides_restantes+=3
            self.grille[2][2]=BonbonNoir(2,2,self)
            self.grille[2][6]=BonbonNoir(6,2,self)
            self.grille[6][2]=BonbonNoir(2,6,self)
            self.grille[6][6]=BonbonNoir(6,6,self)
        elif self.niveau==5:
            self.aides_restantes+=3
            self.grille[2][2]=BonbonNoir(2,2,self)
            self.grille[2][6]=BonbonNoir(2,6,self)
            self.grille[6][2]=BonbonNoir(6,2,self)
            self.grille[6][6]=BonbonNoir(6,6,self)
            self.grille[4][4]=BonbonNoir(4,4,self)
        elif self.niveau==6:
            self.aides_restantes+=3
            self.grille[1][4]=BonbonNoir(4,1,self)
            self.grille[3][1]=BonbonNoir(1,3,self)
            self.grille[3][7]=BonbonNoir(7,3,self)
            self.grille[5][4]=BonbonNoir(4,5,self)
            self.grille[7][2]=BonbonNoir(2,7,self)
            self.grille[7][6]=BonbonNoir(6,7,self)
        elif self.niveau==7: 
            self.aides_restantes+=2
            self.grille[1][2]=BonbonNoir(2,1,self)
            self.grille[1][6]=BonbonNoir(6,1,self)
            self.grille[4][8]=BonbonNoir(8,4,self)
            self.grille[4][4]=BonbonNoir(4,4,self)
            self.grille[4][0]=BonbonNoir(0,4,self)
            self.grille[7][2]=BonbonNoir(2,7,self)
            self.grille[7][6]=BonbonNoir(6,7,self)
        elif self.niveau==8:
            pass
        self.score=0
            
    def test_deja_alignement(self,i,j):
        """Cette fonction teste pour un couple (i,j) de coordonnées donnée, s'il
        est déjà aligné avec des autres bonbons."""
        
        liste=[]
        liste+=(self.grille[i][j].test_alignement_gauche(j,i)[0])
        liste+=(self.grille[i][j].test_alignement_haut(j,i)[0])
        liste=list(set(liste))
        return liste
                    
    def test_possibilite(self):
        """Cette méthode parcour toute la grille à la recherche de déplacement
        possible.
        S'il y en a elle met en surbrillance deux bonbons.
        S'il n'y en a pas elle renvoie un message."""
        
        for i in range (self.__n - 1):
            for j in range (self.__m - 1):
                if (self.grille[i][j].test_alignement_droite(j+1,i)[0])!=[]:
                    res=[i,j,i,j+1]
                    return res
                if (self.grille[i][j].test_alignement_bas(j,i+1)[0])!=[]:
                    res=[i,j,i+1,j]
                    return res
        return (False)
            
    def echange(self,bonbon1,bonbon2,liste_bonbons_exploses):
        """Cette fonction prend en entrée 2 bonbons et une liste des bonbons à explosés.
        Elle est exécutée lorsqu'après avoir selectionne 2 bonbons, des explosions doivent
        avoir lieues.
        Elle échange les coordonnées des bonbons à exploser.
        Une fois cela fait, elle modifie en conséquence la liste des bonbons à exploser
        pour que les coordonnées ne soient pas échanger deux fois.
        La grille est également modifié.
        Elle renvoie la liste des bonbons à explosés """
        
        x1=bonbon1.x
        y1=bonbon1.y
        x2=bonbon2.x
        y2=bonbon2.y
        assert1=False
        assert2=False
        if bonbon1 in liste_bonbons_exploses:
            assert1=True
            liste_bonbons_exploses.remove(bonbon1)
        if bonbon2 in liste_bonbons_exploses:
            assert2=True
            liste_bonbons_exploses.remove(bonbon2)
        bonbon1.x,bonbon2.x=bonbon2.x,bonbon1.x
        bonbon1.y,bonbon2.y=bonbon2.y,bonbon1.y
        if assert1==True:
            liste_bonbons_exploses.append(bonbon1)
        if assert2==True:
            liste_bonbons_exploses.append(bonbon2)
        self.grille[y1][x1],self.grille[y2][x2]=self.grille[y2][x2],self.grille[y1][x1]
        return(liste_bonbons_exploses)
            
    def randombonbon(self,i,j):
        
        """Cette fonction permet de créer un bonbon à l'emplacement (i,j) au hasard 
        dans le but de remplir une des deux grilles. Cela prend en compte le niveau
        dans lequel le joueur situe"""
        
        o=randint(1,7)
        if self.niveau>4:
            o=randint(1,8)
        if o==1:
            a=Bonbon1(j,i,self)
        elif o==2:
            a=Bonbon2(j,i,self)
        elif o==3:
            a=Bonbon3(j,i,self)
        elif o==4:
            a=Bonbon4(j,i,self)
        elif o==5:
            a=Bonbon5(j,i,self)
        elif o==6:
            a=Bonbon6(j,i,self)
        else:
            a=Bonbon7(j,i,self)
        return a
        
    def liste_explosesuper(self,bonbon):
        """ Cette fonction prend en argument un bonbon bonus pour 
        renvoyer la liste des bonbons à exploser présents sur sa ligne et sa 
        colonne"""
        x=bonbon.x
        y=bonbon.y
        L=[]
        for i in range(self.__n):
            L.append(self.grille[i][x])
        for i in range (self.__m):
            L.append(self.grille[y][i])
        return list(set(L))
    def Superoupas(self,liste,l,x,y):
        """Cette fonction permet de savoir si un ou plusieurs BonbonSuper  
        sont adjacents à un alignement de bonbons à exploser; si c'est le cas 
        elle renvoi la liste de ces bonbons"""

        L=[]
        if liste != []: 
            if l=="Hr":
                xmin,xmax= min_maxcoord(liste,l)
                if xmin >= 1 :
                    if self.grille[y][xmin-1].car()== "Bonbon SUPER":
                        L.append(self.grille[y][xmin-1])
                if xmax < (self.__m -1) :
                    if self.grille[y][xmax+1].car()== "Bonbon SUPER":
                        L.append(self.grille[y][xmax+1])
            else: 
                ymin,ymax= min_maxcoord(liste,l)
                if ymin >= 1 :
                    if self.grille[ymin-1][x].car()== "Bonbon SUPER":
                        L.append(self.grille[ymin-1][x])
                if ymax < (self.__n -1) :
                    if self.grille[ymax+1][x].car()== "Bonbon SUPER":
                        L.append(self.grille[ymax+1][x])
        return L 
    
 
    def newliste_explose(self,L):
        """ Cette fonction renvoi la liste des bonbons à exploser à partir des 
        Bonbons Super explosés"""
        liste=[]
        for i in L:
            liste+= self.liste_explosesuper(i)
        return liste    
#                            
     
         
def min_maxcoord(l,mot):
    """ cette fonction permet de connaitre les coordonées minimal et maximal 
    d'un alignement à exploser pour permettre de savoir si un Bonbon Super 
    est adjacent"""

    n= len(l)
    if mot=='Hr':
        minn=100
        maxx=0
        for i in range(n):
            x=l[i].x
            if x>maxx:
                maxx=x
            if x<minn:
                minn=x
    else: 
        minn=100
        maxx=0
        for i in range(n):
            y=l[i].y
            if y>maxx:
                maxx=y
            if y<minn:
                minn=y
    return minn,maxx            
        
        
    
def trier_par_y_decroissant(liste):
    """ Cette fonction renvoie deux listes à partir d'une liste de bonbons :
        -La premiere liste est la liste des bonbons tries par y decroissant, c'est
        a dire le bonbon situé le plus bas est le premier.
        -La seconde liste est la liste des "x" par rapport a la liste deja trie"""
        
    for i in range (1,len(liste)):
        x=liste[i].y
        j=i
        while j>0 and liste[j-1].y<x:
            liste[j-1],liste[j]=liste[j],liste[j-1]
            j-=1
    liste_coords=[]
    for i in range(len(liste)):
        liste_coords.append(liste[i].x)
        liste_coords=list(set(liste_coords))
    return liste, liste_coords
    


    
