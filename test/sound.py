import os
import sys
from PyQt5 import QtCore, QtMultimedia
import time
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def sound():

    filename = os.path.join(CURRENT_DIR, "C:\\Users\\Zeynab\\Downloads\\3times.mp3")
    app2 = QtCore.QCoreApplication(sys.argv)
    player = QtMultimedia.QMediaPlayer()
    url = QtCore.QUrl.fromLocalFile(filename)
    player.setMedia(QtMultimedia.QMediaContent(url))
    player.play()

    sys.exit(app2.exec_())

if __name__ == "__main__":
    sound()