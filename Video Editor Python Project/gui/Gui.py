
from asyncio import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

class WINDOW():
    sizeX = 1280
    sizeY = 720
    positionX = 0
    positionY = 0
    name = "Green Editor"
    def __init__(self, sizeX = 1280,sizeY = 720, positionX = 0, positionY = 0, name = "Green Editor"):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.positionX = positionX
        self.positionY = positionY
        self.name = name
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle(self.name)
        window.resize(self.sizeX, self.sizeY)
        window.move(self.positionX, self.positionY)
        label = QLabel(window)
        label.setText("Hello world!")
        window.show()
        app.exec()

def guiLoad():
    x = WINDOW(sizeX= 200)
    sleep(1)
    
    
