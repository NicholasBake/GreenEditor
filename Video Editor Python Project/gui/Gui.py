
from asyncio import sleep
from multiprocessing import Process
from threading import Thread
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSizePolicy, QGridLayout
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


##### THIS IS FOR MANUAL PLACEMENT ONLY USE IF NECESSARY WONT SCALE WITH WINDOW !!!!!!!!!!!! 
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
    editorWindowLayout = QGridLayout()
    b1 = QLabel("Hello world!")
    b1.setFont(QFont('Times', 30))
    b1.setStyleSheet('QLabel{background-color : red;}')
    editorWindowLayout.addWidget(b1, 0,0,alignment = QtCore.Qt.AlignHCenter)
    editorWindow.window.setLayout(editorWindowLayout)
    editorWindowLayout.activate()
    editorWindow.loadWindow()
    
    
    

