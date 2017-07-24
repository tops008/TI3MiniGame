from PyQt4 import QtGui


class Ship():

    def __init__(self, shipName, color):
        self.shipName = shipName
        self.color=color



    def createOnGrid(self, grid):
        iconName = 'icons/%s %s.png' % (self.color, self.shipName)
        print 'iconName is ' + iconName
        icon = QtGui.QPixmap(iconName)

        self.item = grid.scene.addPixmap(icon)
        self.item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.item.setPos(30, 30)
        self.item.setAcceptDrops(True)
        self.item.scale(0.5, 0.5)


