from PyQt5 import QtWidgets

#Simple vector class, which is drawable as a line
class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)


#Class that implements an object's trajectory, composed of:
#Position: 2D vector that will be incremented by the object's velocity
#Velocity: 2D vector incremented by the object's acceleration
#Acceleration: Vector that can be changed by the object
class Trajectory():
    def __init__(self, pos=Vector(), vel=Vector(), acc=Vector()):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.makeLines()

    def makeLine(self, vec1, vec2):
        return QtWidgets.QGraphicsLineItem(vec1.x, vec1.y, vec2.x, vec2.y)

    def makeLines(self):
        self.vel_line = self.makeLine(self.pos, self.pos+self.vel)
        self.acc_line = self.makeLine(self.pos+self.vel, self.pos+self.vel+self.acc)

    def step(self):
        self.vel += self.acc
        self.pos += self.vel

    def next(self):
        next = Trajectory(self)
        next.step()
        return next

    def create(self, grid):
        #draw the velocity and acceleration lines
        #grid.scene.
        pass
