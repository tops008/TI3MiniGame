from PyQt5 import QtGui, QtWidgets
from Trajectory import *
from ScaledPixmap import *

class GridObject():

    def __init__(self, iconName, traj = Trajectory()):
        self.image = ScaledPixmap(iconName)
        self.traj = traj
        
    def create(self, grid, scale=0.5):
        self.item = grid.scene.addPixmap(self.image.scale(scale))
        self.item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.item.setPos(self.traj.pos.x, self.traj.pos.y)
        self.item.setAcceptDrops(True)

    def step(self):
        self.traj.step()
        self.item.setPos(self.traj.pos.x, self.traj.pos.y)
