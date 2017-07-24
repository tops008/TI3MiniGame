from PyQt4 import QtCore, QtGui
import Global

class Config(QtGui.QWidget):

    def __init__(self):
        super(Config, self).__init__()

        #Setup the grid for the input fields
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        #Color is a drop-down box
        self.color = Global.colors[0]
        self.colorLabel = QtGui.QLabel("Color", self)
        self.colorBox = QtGui.QComboBox(self)
        for color in Global.colors:
            self.colorBox.addItem(color)
        self.grid.addWidget(self.colorLabel, 0, 0)
        self.grid.addWidget(self.colorBox, 0, 1)
        self.colorBox.activated[str].connect(self.colorChoice)

        #Number of ships are line edit fields
        pos=1
        self.nShips = {}
        self.nShipsField = {}
        for ship in Global.ships:
            self.nShips[ship] = QtGui.QLabel(ship+'s')
            self.nShipsField[ship] = QtGui.QLineEdit()
            self.grid.addWidget(self.nShips[ship], pos, 0)
            self.grid.addWidget(self.nShipsField[ship], pos, 1)
            pos += 1

        
        self.setLayout(self.grid)

        
    def colorChoice(self, text):
        self.color = text


    
