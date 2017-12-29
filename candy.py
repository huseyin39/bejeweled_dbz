# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\huseyin\Downloads\candy.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(750, 670)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Quitter = QtGui.QPushButton(self.centralwidget)
        self.Quitter.setGeometry(QtCore.QRect(110, 560, 121, 41))
        self.Quitter.setObjectName(_fromUtf8("Quitter"))
        self.Nouv_partie = QtGui.QPushButton(self.centralwidget)
        self.Nouv_partie.setGeometry(QtCore.QRect(280, 560, 121, 41))
        self.Nouv_partie.setObjectName(_fromUtf8("Nouv_partie"))
        self.Aide = QtGui.QPushButton(self.centralwidget)
        self.Aide.setGeometry(QtCore.QRect(450, 560, 121, 41))
        self.Aide.setObjectName(_fromUtf8("Aide"))
        self.score = QtGui.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(530, 170, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score.setFont(font)
        self.score.setObjectName(_fromUtf8("score"))
        self.score.setStyleSheet("background-color: rgb(250, 220, 255);")
        self.score.setFrameStyle(3)
        self.objectif = QtGui.QLabel(self.centralwidget)
        self.objectif.setGeometry(QtCore.QRect(530, 240, 190, 50))
        self.objectif.setFont(font)
        self.objectif.setObjectName(_fromUtf8("objectif"))
        self.objectif.setStyleSheet("background-color: rgb(250, 220, 255);")
        self.objectif.setFrameStyle(3)
        self.niveau = QtGui.QLabel(self.centralwidget)
        self.niveau.setGeometry(QtCore.QRect(530, 100, 190, 50))
        self.niveau.setFont(font)
        self.niveau.setObjectName(_fromUtf8("objectif"))
        self.niveau.setStyleSheet("background-color: rgb(250, 220, 255);")
        self.niveau.setFrameStyle(3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichiers = QtGui.QMenu(self.menubar)
        self.menuFichiers.setObjectName(_fromUtf8("menuFichiers"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.menuFichiers.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichiers.menuAction())

        QtCore.QObject.connect(self.Quitter, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.actionQuitter, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btn = [[QtGui.QPushButton('', self.centralwidget)
                    for j in range(9)]
                    for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.btn[i][j].setGeometry(QtCore.QRect(50*(j + 1), 50*(i + 1), 51,51))
                self.btn[i][j].setFlat(True) #Permet d'enlever les bordures des boutons
        self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Quitter.setText(_translate("MainWindow", "Quitter", None))
        self.Nouv_partie.setText(_translate("MainWindow", "Nouvelle Partie", None))
        self.Aide.setText(_translate("MainWindow", "Aide", None))
        self.score.setText(_translate("MainWindow", "Score : ", None))
        self.objectif.setText(_translate("MainWindow", "Objectif : ", None))
        self.niveau.setText(_translate("MainWindow", "Niveau : ", None))
        self.menuFichiers.setTitle(_translate("MainWindow", "Fichiers", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

