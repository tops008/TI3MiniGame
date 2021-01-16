from PyQt5 import QtCore, QtGui, QtWidgets
import Global

class Config(QtWidgets.QWidget):

    def __init__(self, config="default.cfg"):
        super(Config, self).__init__()

        #Setup the grid for the input fields
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)

        #Color is a drop-down box
        pos=1
        self.colors=[]
        self.colorLabels=[]
        self.colorBoxes=[]
        for i in range(2):
            self.colors.append(Global.colors[i])
            self.colorLabels.append(QtWidgets.QLabel("Color "+str(i), self))
            self.colorBoxes.append(QtWidgets.QComboBox(self))
            for color in Global.colors:
                self.colorBoxes[i].addItem(color)
                self.grid.addWidget(self.colorLabels[i], pos, 0)
                self.grid.addWidget(self.colorBoxes[i], pos, 1)
                self.colorBoxes[i].activated[str].connect(self.indexedColorChoice(i))

            self.colorBoxes[i].setCurrentText(self.colors[i])
                
            pos += 1
        
        #Number of ships are line edit fields
        self.nShips = {}
        self.nShipsField = {}
        for ship in Global.shipTypes:
            self.nShips[ship] = QtWidgets.QLabel(ship+'s')
            self.nShipsField[ship] = QtWidgets.QLineEdit()
            self.grid.addWidget(self.nShips[ship], pos, 0)
            self.grid.addWidget(self.nShipsField[ship], pos, 1)
            pos += 1

        #Read in the configuration
        with open(config) as file:
            for line in file.readlines():
                line = line.strip()
                if len(line) == 0: continue
                if line[0] == '#': continue
                eles = line.split()
                if len(eles) != 3:
                    print("Warning: Skipping invalid config line:",line)
                    continue
                name, eq, num = eles
                try:
                    self.nShipsField[name].setText(num)
                except KeyError:
                    print("Error: Invalid entry in file:",name,num)
        
        self.setLayout(self.grid)

    def indexedColorChoice(self, index):
        def colorChoice(text):
            self.colors[index] = text
        return colorChoice


    
