from PyQt5 import QtGui, QtWidgets

from GridObject import *

class Ship(GridObject):

    def __init__(self, shipName, color, traj = Trajectory()):
        super().__init__('icons/%s %s.png' % (color, shipName), traj)

        self.shipName = shipName
        self.color=color

    def create(self, grid, pos):
        #this isn't so nice, but it works...
        #self = self.scaled(int(self.width()*0.5), int(self.height()*0.5))
        super().create(grid, pos)






