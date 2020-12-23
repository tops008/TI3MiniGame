import math
from PyQt5 import QtCore, QtGui, QtWidgets

# ==============================================================================
class QRegularPolygon(QtWidgets.QGraphicsPolygonItem):
    """
    Regular polygon of N sides
    """

    def __init__(self, sides, radius, center, angle = None, parent=None):
        """
        Initializes an hexagon of the given radius.
            sides -- sides of the regular polygon
            radius -- radius of the external circle
            center -- QPointF containing the center
            angle -- offset angle in radians for the vertices
        """
        super(QRegularPolygon,self).__init__(parent)

        if sides < 3: 
            raise StandardError ('A regular polygon at least has 3 sides.')
        self._sides = sides
        self._radius = radius
        if angle != None: self._angle = angle
        else: self._angle = 0.0
        self._center = center

        points = list()
        for s in range(self._sides):
            angle = self._angle + (2*math.pi * s/self._sides)
            x = center.x() + (radius * math.cos(angle))
            y = center.y() + (radius * math.sin(angle))
            points.append(QtCore.QPointF(x,y))

        self.setPolygon( QtGui.QPolygonF(points) )




