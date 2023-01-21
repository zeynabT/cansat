
from PyQt5 import QtCore
import secrets
import time



class ProgressWorker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    percentageChanged = QtCore.pyqtSignal(int)

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
        self.percentageChanged.emit(self.percentage)

    def start(self):
        self.started.emit()

    def finish(self):
        self.finished.emit()


class FakeWorker:
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


def long_running_function(foo, baz="1", worker=None):
    if worker is None:
        worker = FakeWorker()
    worker.start()
    while worker.percentage < 100:
        value = secrets.randbelow(99)  # initializing progress bar
        worker.percentage = value
        time.sleep(1)
        worker.finish()