from PyQt5 import QtCore, QtGui, QtWidgets

from Config import *
from Ship import *
from Game import *
import Global

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, settings, grid):
        super().__init__()
        
        self.config = Config()
        self.initUI()
        self.grid=grid

        self.setGeometry(settings['x'],
                         settings['y'],
                         settings['width'],
                         settings['height'])
        
        self.setCentralWidget(self.grid)

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
        self.game = Game()
        self.game.create(self.grid, self.config)
