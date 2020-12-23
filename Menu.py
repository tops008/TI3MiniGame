from PyQt5 import QtCore, QtGui, QtWidgets

from Config import *
from Ship import *
import Global

class Menu(QtWidgets.QMainWindow):

    def __init__(self):
        super(Menu, self).__init__()
        
        self.config = Config()
        self.initUI()

        #Just a list of the ships on the board so they don't get garbage collected
        self.ships = list()
        
    def initUI(self):               
        
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        ###File menu
        fileMenu = menubar.addMenu('&File')

        #Actions for file menu
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        exitAction.triggered.connect(self.config.closeEvent)
        
        newGameAction = QtWidgets.QAction(QtGui.QIcon('newGame.png'), '&New Game', self)        
        newGameAction.setShortcut('Ctrl+N')
        newGameAction.setStatusTip('New Game')
        newGameAction.triggered.connect(self.newGame)


        
        #Add the file menu actions
        fileMenu.addAction(exitAction)
        fileMenu.addAction(newGameAction)

        
        #Settings
        settingsMenu = menubar.addMenu('&Settings')
        
        #Actions for settings
        configAction = QtWidgets.QAction('&Config', self)
        configAction.setShortcut('Ctrl+C')
        configAction.setStatusTip('Open configuration')
        configAction.triggered.connect(self.openConfig)
        
        #Add the settings menu actions
        settingsMenu.addAction(configAction)

        self.setWindowTitle('TI3 Combat Mini-Game')    
        #self.show()


    def openConfig(self):
        self.config.show()

        
    def newGame(self):
        for ship in self.ships:
            self.grid.scene.removeItem(ship.item)
        del self.ships[:]

        #Go through the current config and setup the ships
        for shipName in Global.ships:
            nShips = 0
            txt = self.config.nShipsField[shipName].text()
            if txt != '':
                nShips = int(txt)
                print('Number of ' + shipName + ' is ' + str(nShips))

            for i in range(0, nShips):
                ship = Ship(shipName, self.config.color)
                ship.createOnGrid(self.grid)
                self.ships += [ship]
