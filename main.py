import sys, math
from PyQt4 import QtCore, QtGui

from HexGrid import *
from QRegularPolygon import *
from Menu import *

# ==============================================================================
def main():
    """
    That's it: the  main function
    """

    #Create the application
    app = QtGui.QApplication(sys.argv)


    #Create the hex grid
    radius = 50
    sides = 6
    border=2
    ntilesWide = 7

    grid = HexGrid(QtCore.QRectF(0.0, 0.0, 800, 800))
    grid.addTiles(radius, sides, border, ntilesWide)


    #Create the main menu and add the grid
    menu = Menu()
    menu.setGeometry(100, 0, 800, 800)
    menu.grid = grid
    menu.setCentralWidget(grid)

    
    #Show the menu and execute
    menu.show()
    app.exec_()

# ==============================================================================
if __name__ == '__main__':
    main()

