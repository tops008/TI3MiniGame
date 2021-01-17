from Ship import *
import Global
from Trajectory import *

class Game():

    def __init__(self):
        
        #Just a list of the ships on the board so they don't get garbage collected
        self.ships = list()


    def create(self, grid, config):
        for ship in self.ships:
            self.grid.scene.removeItem(ship.item)
        del self.ships[:]

        #Go through the current config and setup the ships for each player
        pos=[]
        pos.append((30, 30))
        pos.append((30, 770))
        step = 30
        offset = 0
        offsets = {}
        for shipName in Global.shipTypes:
            nShips = 0
            txt = config.nShipsField[shipName].text()
            if txt != '':
                nShips = int(txt)
                print('Number of ' + shipName + ' is ' + str(nShips))

            for player in range(2):
                for i in range(0, nShips):
                    xOffset=0
                    if shipName in offsets:
                        xOffset = offsets[shipName]
                    else:
                        xOffset = offset
                        offset += step
                        offsets[shipName] = xOffset

                    #ship.create(self.grid, (pos[player][0]+xOffset, pos[player][1]))
                    self.ships.append(Ship(shipName, config.colors[player], Trajectory(pos=Vector(pos[player][0]+xOffset, pos[player][1]))))
                    self.ships[len(self.ships)-1].create(grid, 0.5)


    
