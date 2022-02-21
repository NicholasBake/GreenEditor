from asyncio import sleep
from multiprocessing import Process
from threading import Thread
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
import sys

class WINDOW(QWidget):
    
    sizeX = 1280
    sizeY = 720
    positionX = 0
    positionY = 0
    name = "Green Editor"
    app = QApplication(sys.argv)
    window = QWidget()
    def __init__(self, sizeX = 1280,sizeY = 720, positionX = 0, positionY = 0, name = "Green Editor"):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.positionX = positionX
        self.positionY = positionY
        self.name = name
        super().__init__()
    def loadWindow(self):
        self.window.setWindowTitle(self.name)
        self.window.resize(self.sizeX, self.sizeY)
        self.window.move(self.positionX, self.positionY)
        self.window.show()
        self.app.exec()


def setupWidget(widgetToAdd, x = 200, y = 200, w = 200, h = 200, labelText = "", labelFont = 0):
    widgetToAdd.move(x, y)
    widgetToAdd.resize(w, h)
    if labelText != "":
        widgetToAdd.setText(labelText)
        if labelFont != 0:
            widgetToAdd.setFont(QFont('Times', labelFont))
        else:
            widgetToAdd.setFont(QFont('Times', 10))
    widgetToAdd.show()


def guiLoad():
    editorWindow = WINDOW(positionX = 200, sizeX = 1280)
    test = QLabel(editorWindow.window)
    test.setFont(QFont())
    setupWidget(test, labelText = "Hello world!", labelFont= 20)
    editorWindow.loadWindow()
    time.sleep(1)
    
    
    
    
    

