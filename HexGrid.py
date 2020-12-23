import math
from PyQt5 import QtCore, QtGui, QtWidgets
from QRegularPolygon import *

# ==============================================================================
class HexGrid(QtWidgets.QGraphicsView):
    """
    Graphics view for an hex grid.
    """

    # --------------------------------------------------------------------------
    def __init__(self, rect=None, parent=None):
        """
        Initializes an hex grid. This object will be a GraphicsView and it will
        also handle its corresponding GraphicsScene.
            rect -- rectangle for the graphics scene.
            parent -- parent widget
        """
        super(HexGrid,self).__init__(parent)

        self.scene = QtWidgets.QGraphicsScene(self)
        if rect != None: 
            if isinstance(rect, QtCore.QRectF): self.scene.setSceneRect(rect)
            else: raise StandardError ('Parameter rect should be QtCore.QRectF')
        self.setScene(self.scene)



    def addTiles(self, radius, sides, border, ntilesWide):

        ntilesRadius = int(ntilesWide/2+1)
        apothem = radius * math.cos(math.pi/sides)
        side = 2 * apothem * math.tan(math.pi/sides)


        xinit = radius
        yinit = radius
        angle = 0#math.pi/2
        polygons = list()
        
        xoffset=100
        yoffset=100
        
        #start at the top middle, run down, and work your way to the sides
        nRows=ntilesRadius
        for col in range(ntilesWide):
            #figure out where the top is
            for row in range(nRows):
                xcenter=(1+col)*(apothem*2*math.cos(math.pi/sides)+border)+xoffset
                ycenter=(math.fabs(ntilesRadius-col-1)+row*2)*(apothem+border)+yoffset
                #print col, row, xcenter, ycenter
                center = QtCore.QPointF(xcenter,ycenter)
                
                h = QRegularPolygon(sides, radius, center, angle)
                brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
                #brush.setColor(QtWidgets.QColor().setRed(0.0))
                h.setBrush(brush)
                
                polygons.append(h)
                self.scene.addItem(h)
                
            if col < ntilesRadius-1:
                nRows += 1
            else:
                nRows -= 1
        

