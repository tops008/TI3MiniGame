import math
from PyQt5 import QtCore, QtGui, QtWidgets
from QRegularPolygon import *

# ==============================================================================
class HexGrid(QtWidgets.QGraphicsView):
    """
    Graphics view for an hex grid.
    """

    # --------------------------------------------------------------------------
    def __init__(self, settings, rect=None, parent=None):
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
            else: raise Exception ('Parameter rect should be QtCore.QRectF')
        self.setScene(self.scene)

        
        self.radius=settings['radius']
        self.border=settings['border']
        self.nTilesWide=settings['nTilesWide']
        self.sides=6

        self.addTiles()

    def center(self):
        pass

    def addTiles(self):

        nTilesRadius = int(self.nTilesWide/2+1)
        apothem = self.radius * math.cos(math.pi/self.sides)
        side = 2 * apothem * math.tan(math.pi/self.sides)


        xinit = self.radius
        yinit = self.radius
        angle = 0#math.pi/2
        self.polygons = list()
        
        xoffset=100
        yoffset=100
        
        #start at the top middle, run down, and work your way to the sides
        nRows=nTilesRadius
        for col in range(self.nTilesWide):
            #figure out where the top is
            for row in range(nRows):
                xcenter=(1+col)*(apothem*2*math.cos(math.pi/self.sides)+self.border)+xoffset
                ycenter=(math.fabs(nTilesRadius-col-1)+row*2)*(apothem+self.border)+yoffset
                #print col, row, xcenter, ycenter
                center = QtCore.QPointF(xcenter,ycenter)
                
                h = QRegularPolygon(self.sides, self.radius, center, angle)
                brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
                brush.setColor(QtGui.QColor(200,200,200))
                h.setBrush(brush)
                
                self.polygons.append(h)
                self.scene.addItem(h)
                
            if col < nTilesRadius-1:
                nRows += 1
            else:
                nRows -= 1
        

