import random
import time
import sys, os
import numpy as np

from PyQt5 import QtCore, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class SudokuGame(QMainWindow):
    # Class var
    number_set = [[0 for i in range(9)] for j in range(9)]

    def __init__(self):
        # Constructor
        QMainWindow.__init__(self)

        # Load UI
        os.chdir("C:/workspace/Sudoku/qt5")
        loadUi("sudoku.ui", self)

        self.setWindowIcon(QtGui.QIcon("sudoku.png"))
        
        # Connect methods to buttons
        self.btnGenerate.clicked.connect(self.generate)
        # self.btnReset.clicked.connect(self.reset)
        # self.btnSolve.clicked.connect(self.solve)

    def generate(self):
        # Will create solved board first
        pass


    def solve(self):
        # Populate 2d array with numbers
        pass


    def show_board(self):
        # Display 2d array into GUI
        pass


    def reset(self):
        # Reset class 2d array
        self.number_set = [[0 for i in range(9)] for j in range(9)]


app = QApplication([])
window = SudokuGame()
window.show()
app.exec_()
