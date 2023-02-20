
from PyQt5 import QtCore
import time
import config
from PyQt5.QtGui import  QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel

class ImageWorker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    value_change = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._percentage = 0
        value = 0

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if self._percentage == value:
            return
        self._percentage = value
        self.value_change.emit(self.percentage)

    def start(self):
        self.started.emit()

    def finish(self):
        self.finished.emit()


class PWorker:
    def start(self):
        pass

    def finish(self):
        pass

    @property
    def percentage(self):
        return 0

    @percentage.setter
    def percentage(self, value):
        pass


def running_function(event):
    if worker is None:
        worker = PWorker()
    worker.start()
    while True:
        # if who == 'Image':
        #     value = config.pressure
        receivedImage = QLabel()
        pixmap = QPixmap('final.jpg')
        low_rez = QtCore.QSize(321, 200)
        pixmap = pixmap.scaled(low_rez)
        receivedImage.setPixmap(pixmap)
        # imgWidget = self.findChild(QWidget, "widget_7")
        worker.percentage = receivedImage

 
        time.sleep(1)
        worker.finish()
