from PyQt5 import QtCore, QtGui, QtWidgets
import Global

class Config(QtWidgets.QWidget):

    def __init__(self):
        super(Config, self).__init__()

        #Setup the grid for the input fields
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)

        #Color is a drop-down box
        self.color = Global.colors[0]
        self.colorLabel = QtWidgets.QLabel("Color", self)
        self.colorBox = QtWidgets.QComboBox(self)
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
            self.nShips[ship] = QtWidgets.QLabel(ship+'s')
            self.nShipsField[ship] = QtWidgets.QLineEdit()
            self.grid.addWidget(self.nShips[ship], pos, 0)
            self.grid.addWidget(self.nShipsField[ship], pos, 1)
            pos += 1

        
        self.setLayout(self.grid)

        
    def colorChoice(self, text):
        self.color = text


    
