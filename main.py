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
    app = QtGui.QApplication(sys.argv)

    radius = 50
    sides = 6
    border=3
    ntilesWide = 7


    grid = HexGrid(QtCore.QRectF(0.0, 0.0, 800, 800))
    grid.addTiles(radius, sides, border, ntilesWide)



    
    
    testIcon = QtGui.QPixmap('/Users/armbrust/Downloads/tmp/images/white_warsun.png')
    gfxPixItem = grid.scene.addPixmap(testIcon)
    gfxPixItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
    gfxPixItem.setPos(30, 30)
    gfxPixItem.setAcceptDrops(True)
    gfxPixItem.scale(0.5, 0.5)
    #grid.scene.addItem(gfxPixItem)
    #grid.fitInView(gfxPixItem)

    #menu = Menu()
    
    #grid.setScene(grid.scene)
    grid.show()
    app.exec_()

# ==============================================================================
if __name__ == '__main__':
    main()

