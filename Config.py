from PyQt4 import QtCore, QtGui


class Config(QtGui.QWidget):

    def __init__(self):
        super(Config, self).__init__()

        #self.setGeometry(150, 0, 100, 50)

        self.color = QtGui.QLabel("Color")
        self.nWarSuns = QtGui.QLabel("War Suns")
        self.nFighters = QtGui.QLabel("Fighters")

        self.colorEdit = QtGui.QLineEdit()
        self.nWarSunsEdit = QtGui.QLineEdit()
        self.nFightersEdit = QtGui.QLineEdit()
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        
        self.grid.addWidget(self.nWarSuns, 1, 0)
        self.grid.addWidget(self.nWarSunsEdit, 1, 1)

        self.grid.addWidget(self.nFighters, 2, 0)
        self.grid.addWidget(self.nFightersEdit, 2, 1)

        self.grid.addWidget(self.color, 3, 0)
        self.grid.addWidget(self.colorEdit, 3, 1)

        self.setLayout(self.grid)
        


    
