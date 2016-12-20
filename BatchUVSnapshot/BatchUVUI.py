'''
*** UV snapshot each selected object and save those files in given directory (defaults to desktop) with given file format (defaults to maya iff).***

Install instruction:
    -save this script file in your maya script folder. (C:\Users\UserName\Documents\maya\2016\scripts\)

how to use in maya:
    -in the maya script editor, run the following python code to call the UI window:
        from BatchUVSnapshot import BatchUVUI
        ui = BatchUVUI.showUI()
    -select the object(s) that you wish to export the UV of.
    -by default, the UV will be saved on your desktop with the transform name, 1024 x 1024 in resolution, maya iff format.
'''
import os

from maya import cmds
from PySide import QtGui, QtCore


fileExtension = 'png'
userName = os.getenv('username')
defaultDesktopPath = os.path.join('C:\Users\%s' % userName, 'Desktop')
resolutionX = 1024
resolutionY = 1024

############### Logic code
def batchSnapshot(RX=resolutionX, RY=resolutionY, imageFormat=fileExtension, saveFolder=defaultDesktopPath):
    '''
    save UV snapshots of each selected mesh with default values.
    '''
    selectedObj = cmds.ls(sl = True)

    for obj in selectedObj:
        cmds.select(obj, replace=True)
        savePath = os.path.join(saveFolder, '%s.%s' % (obj, imageFormat))
        cmds.uvSnapshot(o=True, n=savePath, xr=RX, yr=RY, ff=imageFormat)

    cmds.select(selectedObj)


############### UI code
class BatchUVUI(QtGui.QWidget):
    '''
    UI window for batch UV snapshot
    in this window you can change any default value to your need. ex.(resolutions, save location, image format)
    for actual file name, it will be named after your mesh's transform node.
    '''
    def __init__(self):
        super(BatchUVUI,self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ImageTypes = ['iff', 'sgi', 'pic', 'tif', 'als', 'gif', 'rla', 'jpg', 'png']
        self.buildUI()

    def buildUI(self):
        '''
        layout for the ui framework
        '''
        self.setWindowTitle('Batch UV Snapshot')
        self.resize(300, 50)

        # first row - resolution input field
        layout = QtGui.QGridLayout(self)
        layout.addWidget(QtGui.QLabel('Resolution'), 0, 0)
        self.RXBox = QtGui.QLineEdit()
        self.RXBox.setText('%s' % (resolutionX))
        layout.addWidget(self.RXBox, 0, 1)
        self.RYBox = QtGui.QLineEdit()
        self.RYBox.setText('%s' % (resolutionY))
        layout.addWidget(self.RYBox, 0, 2)

        # second row - save directory
        layout.addWidget(QtGui.QLabel('Path'), 1, 0)
        self.pathTextBox = QtGui.QLineEdit()
        self.pathTextBox.setText(defaultDesktopPath)
        layout.addWidget(self.pathTextBox, 1, 1, 1, 2)
        self.browserBtn = QtGui.QPushButton('Browser')
        self.browserBtn.clicked.connect(self.browseDirectory)
        layout.addWidget(self.browserBtn, 1, 3)

        # third row - file extension
        self.comboBox = QtGui.QComboBox()
        self.comboBox.addItems(self.ImageTypes)
        layout.addWidget(self.comboBox, 2, 2)

        # third row- savebutton
        self.saveBtn = QtGui.QPushButton('Save')
        layout.addWidget(self.saveBtn, 2, 3)
        self.saveBtn.clicked.connect(self.saveUV)

    def browseDirectory(self):
        ''' call file dialog window to set up the save directory '''
        folderName = QtGui.QFileDialog.getExistingDirectory()
        self.pathTextBox.setText(folderName)

    def saveUV(self):
        ''' save the images with given values (if there is any modified value) '''
        yResolution = int(self.RYBox.text())
        xResolution = int(self.RXBox.text())
        fileExtension = self.comboBox.currentText()
        saveFolder = self.pathTextBox.text()
        batchSnapshot(RX=xResolution, RY=yResolution, imageFormat=fileExtension, saveFolder=saveFolder)


############### call this function in maya to open up the UI
def showUI():
    ui = BatchUVUI()
    ui.show()
    return ui
