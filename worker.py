
from PyQt5 import QtCore
import secrets
import time
import config


class ProgressWorker(QtCore.QObject):
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


def long_running_function(who, baz="0", worker=None):
    if worker is None:
        worker = PWorker()
    worker.start()
    while True:
        if who == 'AirQuality':
            value = config.AirQuality
        if who == 'Pressure':
            value = config.Pressure
        if who == 'UVIndex':
            value = config.UVIndex
        if who == 'Battery':
            value = config.Battery
        worker.percentage = value
        time.sleep(1)
        worker.finish()
