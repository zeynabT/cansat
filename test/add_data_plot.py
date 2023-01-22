import sys
import time
from PyQt5 import QtGui
import pyqtgraph as pg
import numpy as np


class ExPlot(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        desktop = QtGui.QDesktopWidget()
        width = desktop.screenGeometry().width()
        ratio = width / 1920
        self.resize(1400*ratio, 800*ratio)
        
        self.layout=QtGui.QHBoxLayout(self)
        self.plotWidget = pg.GraphicsLayoutWidget(self)
        self.layout.addWidget(self.plotWidget)
        self.plot = self.plotWidget.addPlot(1,1, enableMenu=False)

        self.indexes = {}
        self.counter = 1
        self.time = 0
        x = np.arange(0, 10, 0.01)
        y = np.sin(x)

        plotData = self.plot.plot(x, y)
        self.plotWidget.scene().sigMouseClicked.connect(self.addPoint)
        
    def addPoint(self, event):
        if event.button()==2:
            items = self.plotWidget.scene().items(event.scenePos())
            plot = items[0]
            try:
                data = plot.getData()
                vb = items[1]
                index = int(vb.mapSceneToView(event.scenePos()).x() / 0.01)
                
                
                if index not in self.indexes.values():
                    x = data[0][index]
                    y = data[1][index]
                    point = self.plot.plot([x, ], [y, ], symbol='o',
                                           symbolSize=20, clickable=True,
                                           name=self.counter)
                    
                    point.sigClicked.connect(self.removePoint)
                    self.indexes[self.counter] = index
                    self.counter += 1
            
            #these are thrown if user clicks way to the left/right of the  plotted data
            except (AttributeError, IndexError):
                pass
    
    def removePoint(self, item):
        tdiff = time.time() - self.time
        if tdiff < 1:
            del self.indexes[item.name()]
            self.plot.removeItem(item)
        
        self.time = time.time()
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ExPlot()
    ex.show()
    sys.exit(app.exec_())
        