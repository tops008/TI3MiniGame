from PyQt5 import QtGui, QtWidgets


class Ship():

    def __init__(self, shipName, color):
        self.shipName = shipName
        self.color=color



    def createOnGrid(self, grid, pos):
        iconName = 'icons/%s %s.png' % (self.color, self.shipName)
        icon = QtGui.QPixmap(iconName)
        icon = icon.scaled(int(icon.width()*0.5), int(icon.height()*0.5))
        
        self.item = grid.scene.addPixmap(icon)
        self.item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.item.setPos(pos[0], pos[1])
        self.item.setAcceptDrops(True)



