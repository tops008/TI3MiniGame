from PyQt4 import QtCore, QtGui

from Config import *
from WarSun import *

class Menu(QtGui.QMainWindow):

    def __init__(self):
        super(Menu, self).__init__()
        
        self.initUI()
        self.config = Config()

        #Just a list of the ships on the board so they don't get garbage collected
        self.ships = list()
        
    def initUI(self):               
        
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        ###File menu
        fileMenu = menubar.addMenu('&File')

        #Actions for file menu
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        newGameAction = QtGui.QAction(QtGui.QIcon('newGame.png'), '&New Game', self)        
        newGameAction.setShortcut('Ctrl+N')
        newGameAction.setStatusTip('New Game')
        newGameAction.triggered.connect(self.newGame)


        
        #Add the file menu actions
        fileMenu.addAction(exitAction)
        fileMenu.addAction(newGameAction)

        
        #Settings
        settingsMenu = menubar.addMenu('&Settings')
        
        #Actions for settings
        configAction = QtGui.QAction('&Config', self)
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
        del self.ships[:]

        #Go through the current config and setup the ships
        nWarSun = int(self.config.nWarSunsEdit.text())

        for i in range(0, nWarSun):
            warsun = WarSun()
            warsun.setColor(str(self.config.colorEdit.text()))
            warsun.createOnGrid(self.grid)
            self.ships += [warsun]
