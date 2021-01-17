from PyQt5 import QtGui

class ScaledPixmap(QtGui.QPixmap):
    def __init__(self, iconName, scale=1):
        super().__init__(iconName)
        if scale != 1: self.scale(scale)

    def scale(self, scale):
        if scale != 1: self = self.scaled(int(self.width()*scale),
                                          int(self.height()*scale))

        return self
