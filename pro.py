
import sys
import threading

from PyQt5 import QtCore, QtWidgets


class PercentageWorker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    percentageChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._percentage = 0

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


import time


def long_running_function(foo, baz="1", worker=None):
    if worker is None:
        worker = FakeWorker()
    worker.start()
    while worker.percentage < 100:
        worker.percentage += 1
        print(foo, baz)
        time.sleep(1)
        worker.finish()


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.progress = QtWidgets.QProgressBar()
        self.button = QtWidgets.QPushButton("Start")

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.button)
        lay.addWidget(self.progress)

        self.button.clicked.connect(self.launch)

    def launch(self):
        worker = PercentageWorker()
        worker.percentageChanged.connect(self.progress.setValue)
        threading.Thread(
            target=long_running_function,
            args=("foo",),
            kwargs=dict(baz="baz", worker=worker),
            daemon=True,
        ).start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())