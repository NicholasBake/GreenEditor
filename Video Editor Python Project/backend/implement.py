import sys
sys.path.append("..")
import gui.Gui
from PyQt5.QtWidgets import QFileDialog

# String that holds path of selected folder in setup step
fileDir = ""
# Function that holds the code for the selectDirectoryButton of gui.Gui 
def selectDirClick():
    # Creating a filedialog so the user can select a directory

    fileDialog = QFileDialog()
    fileDialog.setFileMode(QFileDialog.Directory)
    fileDialog.show()

    # Code for when the file is selected
    fileDir = fileDialog.getExistingDirectory()
    if fileDialog != "":
        gui.Gui.selectDirectoryButton.setText(fileDir)
# Function that holds the code for the createProjectButton of gui.Gui
def createProjClick():
    # Creating the file
    try:
        with open(gui.Gui.selectDirectoryButton.text() + "\\ test.txt", "w") as f:
            f.write("Hello world!")
            print("Created necessary files")
    except FileNotFoundError:
        print("The '" + gui.Gui.selectDirectoryButton.text() + "' Directory doesn't exist!")
    # Exiting setup window
    gui.Gui.setUpWindow.window.close()

    
    

def loadBackendSetUp():
    gui.Gui.selectDirectoryButton.clicked.connect(selectDirClick)
    gui.Gui.createProjectButton.clicked.connect(createProjClick)