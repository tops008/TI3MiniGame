import json

class Settings():

    def __init__(self, fileName):
        """
        Various settings for the layout of the board
        """
        
        self.fileName=fileName
        
        try:
            self.data = json.load(open(self.fileName))
        except FileNotFoundError:
            print("Settings file not found")
        
        self.write()

    def write(self):

        json.dump(self.data, open('check_'+self.fileName,'w+'),indent=4)

