import random
import time
import sys, os

from PyQt5 import QtCore, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class SudokuGame(QMainWindow):
    
    def __init__(self):
        # Constructor
        QMainWindow.__init__(self)

        # Load UI
        os.chdir("C:/workspace/Sudoku/qt5")
        loadUi("sudoku.ui", self)

        self.setWindowIcon(QtGui.QIcon("sudoku.png"))
        
        # Connect methods to buttons :
        # self.btnGenerate.clicked.connect(self.generate)
        # self.btnReset.clicked.connect(self.reset)
        # self.btnSolve.clicked.connect(self.solve)


app = QApplication([])
window = SudokuGame()
window.show()
app.exec_()
