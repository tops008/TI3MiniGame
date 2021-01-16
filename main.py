import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets

from HexGrid import *
from MainWindow import *
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
                                 settings.data['Window']['width'],
                                 settings.data['Window']['height']))


    #Create the main menu and add the grid
    window = MainWindow(settings.data['Window'], grid)

    
    #Show the menu and execute
    window.show()
    app.exec_()

# ==============================================================================
if __name__ == '__main__':
    main()

