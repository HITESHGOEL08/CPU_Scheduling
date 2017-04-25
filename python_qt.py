import operator
import os
import sys

path = os.getcwd()

import pyglet.media as media
from PyQt4 import QtGui, uic, QtTest
from PyQt4.QtGui import QMessageBox
from PyQt4.phonon import Phonon

print(path)

qtCreatorFile = path + "/main.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def EXIT():
    sys.exit()


# def algo():
#     OS = platform.system()
#     if OS == "Linux":
#         osCommandString = "/usr/bin/gedit " + path + "/try.txt"
#     if OS == "Windows":
#         osCommandString = "notepad.exe " + path + "/try.txt"

#    os.system(osCommandString)


class MyApp(QtGui.QMainWindow, Ui_MainWindow, QtGui.QWidget, Phonon.MediaObject):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # Phonon.MediaObject.__init__(self)
        self.setupUi(self)

        self.round_robin.clicked.connect(self.RoundRobin)
        self.sjf.clicked.connect(self.ShortestJobFirst)
        self.fcfs.clicked.connect(self.FirstComeFirstServe)
        self.prior.clicked.connect(self.Prior)
        self.exit.clicked.connect(EXIT)


        self.fname1 = path + '/Sounds/Sound1.mp3'
        self.fname2 = path + '/Sounds/Sound2.mp3'
        self.fname3 = path + '/Sounds/Sound3.mp3'
        self.fname4 = path + '/Sounds/Sound4.mp3'

        self.src1 = media.load(self.fname1)
        self.src2 = media.load(self.fname2)
        self.src3 = media.load(self.fname3)
        self.src4 = media.load(self.fname4)

        self.player1 = media.Player()
        self.player2 = media.Player()
        self.player3 = media.Player()
        self.player4 = media.Player()

        self.player1.queue(self.src1)
        self.player2.queue(self.src2)
        self.player3.queue(self.src3)
        self.player4.queue(self.src4)

        self.player1.volume = 1.0
        self.player2.volume = 1.0
        self.player3.volume = 1.0
        self.player4.volume = 1.0

    def showdialog(self, string):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("One or more fields needs attention!!")
        msg.setInformativeText("Fields unused")
        msg.setWindowTitle("ERROR")
        msg.setDetailedText("The details are as follows:\n\n" + string + " CANNOT BE NULL")
        msg.exec_()
        # print "value of pressed message box button:", retval

    def RoundRobin(self):
        print("Round Robin")
        # subprocess.call(path+"/second.py", shell=True)
        if self.exec.isChecked():
            quantum = self.textEdit.text()
            if quantum == "":
                print("Empty")
                self.showdialog("Round Robin time quantum")
                return
            else:
                quantum = int(quantum)

            duration = []
            for i in range(4):
                duration.append(eval("self.src{}.duration".format(i + 1)))

            print(duration)

            while 1:
                if not all(v == 0 for v in duration):
                    print("in loop")
                    for i in range(4):

                        if duration[i] >= float(quantum) and eval("self.player{}.playing".format(i + 1)) == False:

                            eval("self.player{}.play()".format(i + 1))
                            QtTest.QTest.qWait(quantum * 1000)
                            eval("self.player{}.pause()".format(i + 1))

                            duration[i] -= quantum
                        else:
                            eval("self.player{}.play()".format(i + 1))
                            QtTest.QTest.qWait(quantum * 1000)
                            eval("self.player{}.pause()".format(i + 1))
                            duration[i] = 0
                else:
                    print("break")
                    break

            print(duration)

        else:
            os.system("python " + path + "/dialog.py rr")

    def ShortestJobFirst(self):
        print("Shortest Job First")
        if self.exec.isChecked():
            duration = {}
            for i in range(4):
                # Duration.append(eval("self.src{}.duration".format(i+1)))
                duration["{}".format(i + 1)] = eval("self.src{}.duration".format(i + 1))

            duration = sorted(duration.items(), key=operator.itemgetter(1))

            for i in range(4):
                eval("self.player" + str(duration[eval("{}".format(i))][0]) + ".play()")
                QtTest.QTest.qWait(duration[eval("{}".format(i))][1] * 1000)

            print(duration)

        else:
            os.system("python " + path + "/dialog.py sjf")

    def FirstComeFirstServe(self):
        print("First Come First Serve")
        if self.exec.isChecked():
            for i in range(4):
                eval("self.player{}.play()".format(i + 1))
                # time.sleep(eval("self.src{}.duration".format(i+1)))
                QtTest.QTest.qWait(eval("self.src{}.duration".format(i + 1)) * 1000)

        else:
            os.system("python " + path + "/dialog.py fcfs")

    def Prior(self):
        print("prior")
        if self.exec.isChecked():
            pri = []
            try:
                for i in range(4):
                    pri.append(eval("int(self.pri{}.text())".format(i + 1)))

            except:
                self.showdialog("Priority sequence skipped OR")
                return

            print(pri)

            for i in range(4):
                eval("self.player" + str(pri[i]) + ".play()")
                # time.sleep(eval("self.src{}.duration".format(i+1)))
                QtTest.QTest.qWait(eval("self.src" + str(pri[i]) + ".duration") * 1000)

        else:
            os.system("python " + path + "/dialog.py prior")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


