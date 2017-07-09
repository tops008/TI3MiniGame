from PyQt4 import QtGui


class Ship():

    def __init__(self):
        self.color='white'



    def createOnGrid(self, grid):
        icon = QtGui.QPixmap('images/%s_warsun.png' % self.color)

        self.item = grid.scene.addPixmap(icon)
        self.item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.item.setPos(30, 30)
        self.item.setAcceptDrops(True)
        self.item.scale(0.5, 0.5)

        

    def setColor(self, color):
        self.color=color
