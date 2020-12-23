from PyQt5 import QtGui, QtWidgets


class Ship():

    def __init__(self, shipName, color):
        self.shipName = shipName
        self.color=color



    def createOnGrid(self, grid):
        iconName = 'icons/%s %s.png' % (self.color, self.shipName)
        print('iconName is ' + iconName)
        icon = QtGui.QPixmap(iconName)
        icon = icon.scaled(int(icon.width()*0.5), int(icon.height()*0.5))
        
        self.item = grid.scene.addPixmap(icon)
        self.item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.item.setPos(30, 30)
        self.item.setAcceptDrops(True)
        #self.item.scaled(0.5, 0.5)


