from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSizePolicy, QGridLayout, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
import sys
import os
sys.path.append('..')
import backend.implement




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
    def __del__(self):
        self.name = ""
        self.positionX = 0
        self.positionY = 0
        self.sizeX = 0
        self.sizeY = 0
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
    # Creating setup window, where you can set name of project and where to save it
    global setUpWindow 
    setUpWindow = WINDOW(positionX=0, positionY=0, name="Setup")
    
    # Main layout
    
    setUpWindowLayout = QVBoxLayout()
    setUpWindowLayout.setContentsMargins(200,0,200,0)

    # Welcome text at the top-middle of setUpWindow.window
    global welcome
    welcome = QLabel("Welcome to GreenEditor!")
    welcome.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    welcome.setFont(QFont('Times', 40, 20))
    setUpWindowLayout.addWidget(welcome, alignment=QtCore.Qt.AlignHCenter)
    
    
    # Button that once clicked will create required files in selected directory
    global createProjectButton
    createProjectButton = QPushButton("Create Project")

    # Button that once clicked will open file explorer that user will use to select wanted directory
    global selectDirectoryButton
    selectDirectoryButton = QPushButton("...")
    selectDirectoryButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
    # Secondary layout for input boxes (filepath selection, actually creating the project button)
    inputLayout = QHBoxLayout()
    inputLayout.setContentsMargins(100,0,100,0)
    inputLayout.addWidget(selectDirectoryButton, alignment=QtCore.Qt.AlignVCenter)
    inputLayout.addWidget(createProjectButton, alignment=QtCore.Qt.AlignVCenter)
    setUpWindowLayout.addLayout(inputLayout)
    

    
    setUpWindow.window.setLayout(setUpWindowLayout)
    backend.implement.loadBackendSetUp()
    setUpWindow.loadWindow()

    # Creating a temporary QWidget to store the layout of setUpWindow
    temp = QWidget()
    temp.setLayout(setUpWindowLayout)
    
    # Creating actual Editing window
    editorWindow = WINDOW(positionX = 0, sizeX = 1280, name="Green Editor")
    editorWindowLayout = QGridLayout()
    b1 = QLabel(selectDirectoryButton.text())
    b1.setFont(QFont('Times', 30))
    b2 = QPushButton("Hello world!")
    b3 = QPushButton("Hello world1")
    b2.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
    b3.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
    editorWindowLayout.addWidget(b1, 0,0,alignment= QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
    editorWindowLayout.addWidget(b2, 2, 0)
    editorWindowLayout.addWidget(b3, 1, 0)
    editorWindow.window.setLayout(editorWindowLayout)
    editorWindow.loadWindow()
    
    
    

