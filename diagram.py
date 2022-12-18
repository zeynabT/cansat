from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        

        hour = [1,2,3,4,4]
        temperature = [30,32,34,32,33]

        self.graphWidget.setBackground('w')
        self.graphWidget.plot(hour, temperature)
        self.graphWidget.setGeometry(100, 100, 321, 161)
        #self.centralWidget().resize(321, 161)
        #self.graphWidget.set(321, 161)
        #.setGeometry(100, 100, 600, 500)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()