import os
import platform

import sys
from PyQt4 import QtGui, uic, QtTest

path = os.getcwd()
print(path)

qtCreatorFile = path + "/dialog.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Dialog(QtGui.QMainWindow, Ui_MainWindow, QtGui.QWidget):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.cpp.clicked.connect(self.CPP)
        self.java.clicked.connect(self.JAVA)
        self.python.clicked.connect(self.PYTHON)

    def CPP(self):
        OS = platform.system()
        if OS == "Linux":
            osCommandString = "/usr/bin/gedit "+path+"/Algo/C++/"+sys.argv[1]+".txt"
            print(osCommandString)
        if OS == "Windows":
            osCommandString = "Notepad.exe " + path + "/Algo/C++/"+sys.argv[1]+".txt"

        os.system(osCommandString)

    def JAVA(self):
        OS = platform.system()
        if OS == "Linux":
            osCommandString = "/usr/bin/gedit " + path + "/Algo/Java/" + sys.argv[1] + ".txt"
        if OS == "Windows":
            osCommandString = "Notepad.exe " + path + "/Algo/Java/" + sys.argv[1] + ".txt"

        os.system(osCommandString)

    def PYTHON(self):
        OS = platform.system()
        if OS == "Linux":
            osCommandString = "/usr/bin/gedit " + path + "/Algo/Python/" + sys.argv[1] + ".txt"
        if OS == "Windows":
            osCommandString = "Notepad.exe " + path + "/Algo/Python/" + sys.argv[1] + ".txt"

        os.system(osCommandString)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec_())