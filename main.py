import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets

from HexGrid import *
from QRegularPolygon import *
from Menu import *
from Settings import *

# ==============================================================================
def main():
    """
    That's it: the  main function
    """

    #Create the application
    app = QtWidgets.QApplication(sys.argv)


    #Open settings
    settings = Settings('settings.json')
    
    #Create the hex grid
    grid = HexGrid(settings.data['HexGrid'],
                   QtCore.QRectF(0.0, 0.0,
                                 settings.data['Menu']['width'],
                                 settings.data['Menu']['height']))


    #Create the main menu and add the grid
    menu = Menu()
    menu.setGeometry(settings.data['Menu'])
    menu.grid = grid
    menu.setCentralWidget(grid)

    
    #Show the menu and execute
    menu.show()
    app.exec_()

# ==============================================================================
if __name__ == '__main__':
    main()

