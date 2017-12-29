# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2017

@author: KIZIL- KHALILE
"""

import sys
from PyQt4 import QtGui, QtCore
from candy import Ui_MainWindow
from grille import *


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_MainWindow()
        A=Grille(9,9)
        A.remplir()
        self.grille=A
        self.ui.setupUi(self)
        self.bonbons_choisis=[]
        self.icone_dic = {"Bonbon1" : 'Krilin.png',
                          "Bonbon2" : 'MutenRoshi.png',
                          "Bonbon3" : 'Piccolo.png',
                          "Bonbon4" : 'SonGohan.png',
                          "Bonbon5" : 'SonGoku.png',
                          "Bonbon6" : 'Vegeta.png',
                          "Bonbon7" : 'Gorille.png',
                          "Bonbon Noir" : 'boule4.png',
                          "Bonbon SUPER" : 'buu.png',
                          "Bonbon Genial": 'oolong.png'
                          
                          } 
        self.ui.Aide.setText("Aide ("+str(self.grille.aides_restantes)+")")
        self.ui.score.setText("Score : " +str(self.grille.score)+" Points")
        self.ui.objectif.setText( "Objectif : " +str(self.grille.niv_dic[self.grille.niveau])+" Points")
        self.ui.niveau.setText( "Niveau : " +str(self.grille.niveau))
        # Recommencer - La partie 
        self.ui.Nouv_partie.clicked.connect(self.reset)
        self.ui.Aide.clicked.connect(self.aide_moi)         
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("arrierPlan.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh_grille)
        
        # Affichage des bonbons 
        for i in range(9):
            for j in range(9):
                self.icone(i,j)       
        for i in range(9):
            for j in range(9):
                self.ui.btn[i][j].clicked.connect(self.bouton_clique) 
                self.ui.btn[i][j].valeur = self.grille.grille[i][j]
                self.ui.btn[i][j].setEnabled(True)
                
    def reset(self):
        """ C'est la fonction qui permet de recommencer une partie.
        Elle remet à zéro le score et met en place une nouvelle grille."""
        self.grille.niveau=1
        self.grille.score=0
        self.grille.remplir()
        self.refresh_grille()
    def refresh_grille(self): 
        """ Cette méthode permet d'actualiser l'affichage de la grille
        via la méthode 'icone'.
        Le score est également rafraichît."""
        if self.timer.isActive :
                 self.timer.stop()
        for j in range(self.grille.dimension[1]):
            for i in range(self.grille.dimension[0]):
                self.icone(i,j)
                self.ui.btn[i][j].valeur = self.grille.grille[i][j]
                self.ui.btn[i][j].setEnabled(True)
        self.ui.score.setText("Score : " +str(self.grille.score)+ " Points")
        self.ui.objectif.setText( "Objectif : " +str(self.grille.niv_dic[self.grille.niveau])+" Points")
        self.ui.Aide.setText("Aide ("+str(self.grille.aides_restantes)+")")
        self.ui.niveau.setText( "Niveau : " +str(self.grille.niveau))
    
    def icone(self,i,j):
        """Cette méthode permet d'affecter à chaque icône une image via le dictionnaire.
        Ces images représentent les bonbons"""
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.icone_dic[self.grille.grille[i][j].car()]))
        self.ui.btn[i][j].setIcon(icon)
        self.ui.btn[i][j].setIconSize(QtCore.QSize(50,50))
           
    # Lorsque le joueur clique sur un bonbon          
    def bouton_clique(self):
        """ Cette méthode est appelé lorsque le joueur clique sur un bouton.
        Elle fait ensuite appel à la méthode mouvement()"""
             
        sender = self.sender()
        bonbon_clique = sender.valeur
        if bonbon_clique.car() !="Bonbon Genial":
            sender.setEnabled(False)
        self.mouvement(bonbon_clique)  
            
    # Permet d'effectuer une action
    def mouvement(self,index):
        """Cette méthode est appelé via la méthode bouton_clique().
        Si c'est le premier bonbon sélectionné, on l'ajoute à bonbons_choisis.
        Si dans la liste bonbons_choisis il y a déjà un bonbon, alors on applique
        la méthode bouger() de grille pour effectuer le potentiel mouvement.
        Ensuite on rafraichît la grille."""
        
        if( len(self.bonbons_choisis) == 0):
            self.bonbons_choisis.append(index)
        elif (len(self.bonbons_choisis) == 1):
            self.bonbons_choisis.append(index)
            self.grille.bouger(self.bonbons_choisis[1], self.bonbons_choisis[0])
            self.refresh_grille()  
            self.bonbons_choisis =[]
            if self.grille.niv_dic[self.grille.niveau]<=self.grille.score:
                self.grille.niveau+=1
                self.grille.remplir()   
                self.refresh_grille()
                
    def aide_moi(self):
        """ Cette méthode permet d'afficher deux bonbons entrainanaint une explosion
        si on les inverse. Cela constitute l'aide"""
        
        if self.grille.aides_restantes>0:
            self.grille.aides_restantes-=1
            a=self.grille.test_possibilite()
            if a==False:
                print ('Le jeu va être relancé')
                self.reset()
            else :
                self.ui.btn[a[0]][a[1]].setEnabled(False)
                self.ui.btn[a[2]][a[3]].setEnabled(False)
                self.timer.start(3000)


    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
