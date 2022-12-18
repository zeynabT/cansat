from PyQt5 import QtWidgets, uic 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PySide2 import QtCore, QtWidgets, QtGui
#from PySide2extn.RoundProgressBar import roundProgressBar
#from PySide6 import QtCore
import sys
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import time
from threading import Thread
import secrets

#from PySide2 import QtCore, QtWidgets, QtGui
#from PySide2extn.RoundProgressBar import roundProgressBar

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\CAN-SAT2.ui', self)
        
        A_angular = "12"
        A_linear = "20"
        
        Pressure = "80"
        Pressure_1 = "1"
        Pressure_2 = "2"
        Pressure_3 = "3"
        Pressure_4 = "4"
        Pressure_5 = "5"
        Pressure_6 = "6"
        
        InTemp = "2"
        InTemp_1 = "1"
        InTemp_2 = "2"
        InTemp_3 = "3"
        InTemp_4 = "4"
        InTemp_5 = "5"
        InTemp_6 = "6"
        
        OutTemp = "3"
        OutTemp_1 = "13"
        OutTemp_2 = "14"
        OutTemp_3 = "15"
        OutTemp_4 = "16"
        OutTemp_5 = "17"
        OutTemp_6 = "18"
        
        Hiumidity = "7"
        Hiumidity_1 = "8"
        Hiumidity_2 = "9"
        Hiumidity_3 = "10"
        Hiumidity_4 = "11"
        Hiumidity_5 = "12"
        Hiumidity_6 = "13"

        AirQuality = "4"
        UVIndex = "6"
        
        CoordinateX = 37.8199286
        CoordinateY = -122.4782551
        Coordinate_x = str(CoordinateX)
        Coordinate_y =  str(CoordinateY)
        coordinate = (CoordinateX, CoordinateY)
        
        # todo make label for every int
        self.LA_angular = self.findChild(QLabel, "label_96")
        self.LA_angular.setText(A_angular)
        self.LA_linear = self.findChild(QLabel, "label_97")
        self.LA_linear.setText(A_linear)
        
        self.LPressure = self.findChild(QLabel, "label_2")
        self.LPressure.setText(Pressure)
        self.LPressure_1 = self.findChild(QLabel, "label_67")
        self.LPressure_1.setText(Pressure_1)
        self.LPressure_2 = self.findChild(QLabel, "label_69")
        self.LPressure_2.setText(Pressure_2)
        self.LPressure_3 = self.findChild(QLabel, "label_71")
        self.LPressure_3.setText(Pressure_3)
        self.LPressure_4 = self.findChild(QLabel, "label_73")
        self.LPressure_4.setText(Pressure_4)
        self.LPressure_5 = self.findChild(QLabel, "label_75")
        self.LPressure_5.setText(Pressure_5)
        self.LPressure_6 = self.findChild(QLabel, "label_77")
        self.LPressure_6.setText(Pressure_6)
        
        self.LInTemp = self.findChild(QLabel, "label")
        self.LInTemp.setText(InTemp)
        self.LInTemp_1 = self.findChild(QLabel, "label_25")
        self.LInTemp_1.setText(InTemp_1)
        self.LInTemp_2 = self.findChild(QLabel, "label_27")
        self.LInTemp_2.setText(InTemp_2)
        self.LInTemp_3 = self.findChild(QLabel, "label_29")
        self.LInTemp_3.setText(InTemp_3)
        self.LInTemp_4 = self.findChild(QLabel, "label_31")
        self.LInTemp_4.setText(InTemp_4)
        self.LInTemp_5 = self.findChild(QLabel, "label_33")
        self.LInTemp_5.setText(InTemp_5)
        self.LInTemp_6 = self.findChild(QLabel, "label_35")
        self.LInTemp_6.setText(InTemp_6)
        
        self.LOutTemp = self.findChild(QLabel, "label_37")
        self.LOutTemp.setText(OutTemp)
        self.LOutTemp_1 = self.findChild(QLabel, "label_39")
        self.LOutTemp_1.setText(OutTemp_1)
        self.LOutTemp_2 = self.findChild(QLabel, "label_41")
        self.LOutTemp_2.setText(OutTemp_2)
        self.LOutTemp_3 = self.findChild(QLabel, "label_43")
        self.LOutTemp_3.setText(OutTemp_3)
        self.LOutTemp_4 = self.findChild(QLabel, "label_45")
        self.LOutTemp_4.setText(OutTemp_4)
        self.LOutTemp_5 = self.findChild(QLabel, "label_47")
        self.LOutTemp_5.setText(OutTemp_5)
        self.LOutTemp_6 = self.findChild(QLabel, "label_49")
        self.LOutTemp_6.setText(OutTemp_6)
        
        self.LHiumidity = self.findChild(QLabel, "label_50")
        self.LHiumidity.setText(Hiumidity)
        self.LHiumidity_1 = self.findChild(QLabel, "label_54")
        self.LHiumidity_1.setText(Hiumidity_1)
        self.LHiumidity_2 = self.findChild(QLabel, "label_56")
        self.LHiumidity_2.setText(Hiumidity_2)
        self.LHiumidity_3 = self.findChild(QLabel, "label_58")
        self.LHiumidity_3.setText(Hiumidity_3)
        self.LHiumidity_4 = self.findChild(QLabel, "label_60")
        self.LHiumidity_4.setText(Hiumidity_4)
        self.LHiumidity_5 = self.findChild(QLabel, "label_62")
        self.LHiumidity_5.setText(Hiumidity_5)
        self.LHiumidity_6 = self.findChild(QLabel, "label_64")
        self.LHiumidity_6.setText(Hiumidity_6)
        
        self.LAirQuality = self.findChild(QLabel, "label_52")
        self.LAirQuality.setText(AirQuality)
        
        self.LUVIndex = self.findChild(QLabel, "label_100")
        self.LUVIndex.setText(UVIndex)
        
        self.Coordinate_x = self.findChild(QLabel, "label_103")
        self.Coordinate_x.setText(Coordinate_x)
        self.Coordinate_y = self.findChild(QLabel, "label_105")
        self.Coordinate_y.setText(Coordinate_y)
        
        radioButton_1 = self.findChild(QRadioButton, "radioButton")
        #self.radioButton_1.setStyleSheet("background-color : lightgreen")
        #radioButton_1.setStyleSheet("background-color: red; border: 1rem solid black")
        

        radioButton_2 = self.findChild(QRadioButton, "radioButton_7")
        #self.radioButton_1.setStyleSheet("background-color : lightgreen")
        #radioButton_2.setStyleSheet("background-color: red")
        #window title 
        self.iconText = self.setWindowTitle("FUM_CAN")
        self.windowIcon = self.setWindowIcon(QtGui.QIcon('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\logo-white.jpg'))
        
        
        #icon
        IPressure = self.findChild(QLabel, "label_5")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\pressure.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IPressure.setPixmap(pixmap)
        
        IAcceleration = self.findChild(QLabel, "label_6")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\Acceleration.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IAcceleration.setPixmap(pixmap)
        
        IInTemp = self.findChild(QLabel, "label_7")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\icons8-temperature-inside2.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IInTemp.setPixmap(pixmap)
        
        IIOutTemp = self.findChild(QLabel, "label_8")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\temperature-outside2.jpg')
        pixmap = pixmap.scaled(low_rez)
        IIOutTemp.setPixmap(pixmap)
        
        IHiumidity = self.findChild(QLabel, "label_9")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\humidity-.jpg')
        pixmap = pixmap.scaled(low_rez)
        IHiumidity.setPixmap(pixmap)
        
        IAirQuality = self.findChild(QLabel, "label_10")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\wind2.jpg')
        pixmap = pixmap.scaled(low_rez)
        IAirQuality.setPixmap(pixmap)
        
        IUVIndex = self.findChild(QLabel, "label_11")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\sun.jpg')
        pixmap = pixmap.scaled(low_rez)
        IUVIndex.setPixmap(pixmap)
        
        ISensor = self.findChild(QLabel, "label_12")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\sensor.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor.setPixmap(pixmap)
        
        ISensor_pressure = self.findChild(QLabel, "label_78")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\pressure.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        ISensor_pressure.setPixmap(pixmap)
        
        ISensor_acceleration = self.findChild(QLabel, "label_82")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\Acceleration.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_acceleration.setPixmap(pixmap)
        
        ISensor_temp = self.findChild(QLabel, "label_84")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\icons8-temperature-inside2.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_temp.setPixmap(pixmap)
        
        ISensor_hiumidity = self.findChild(QLabel, "label_79")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\humidity-.jpg')
        low_rez = QtCore.QSize(23, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_hiumidity.setPixmap(pixmap)
        
        ISensor_air = self.findChild(QLabel, "label_83")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\wind2.jpg')
        low_rez = QtCore.QSize(21, 21)
        pixmap = pixmap.scaled(low_rez)
        ISensor_air.setPixmap(pixmap)
        
        ISensor_UV = self.findChild(QLabel, "label_85")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\sun.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_UV.setPixmap(pixmap)
        
        ISatellite_1 = self.findChild(QLabel, "label_80")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\satellite.jpg')
        low_rez = QtCore.QSize(23, 23)
        pixmap = pixmap.scaled(low_rez)
        ISatellite_1.setPixmap(pixmap)
        
        ISatellite_2 = self.findChild(QLabel, "label_81")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\satellite.jpg')
        pixmap = pixmap.scaled(low_rez)
        ISatellite_2.setPixmap(pixmap)
            
        ILogo = self.findChild(QLabel, "label_107")
        pixmap = QPixmap('D:\VSCodeFile\pythonFile\FUM-CAN-new\FUM-CAN\logo.jpg')
        low_rez = QtCore.QSize(50, 45)
        pixmap = pixmap.scaled(low_rez)
        ILogo.setPixmap(pixmap)
        
        # Map
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        webView.setParent(self.findChild(QWidget, "widget_9"))
        webView.setStyleSheet("border-radius: 30px;")
       
        #self.label.setStyleSheet("color: lightgreen")
        #font.setStyle("color: red")
		#font.setFamily("B Nazanin")
		#font.setPointSize(24)
		#self.temp_name.setFont(font)
        
        self.show()
    #def text(self):

class MyApp(QWidget):
    def __init__(self, webveiw):
        self.webview = webveiw
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')
        self.window_width, self.window_height = 1000, 1000
        self.setMinimumSize(self.window_width, self.window_height)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        x = 37.8199286
        y = -122.4782551
        coordinate = (x, y)
        
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webview = QWebEngineView()
        webview.setHtml(data.getvalue().decode())
        layout.addWidget(webview)
        self.show()
        
app =  QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
#acceleration = 0


if __name__ == "__main__":
  Ui()
  app = QApplication(sys.argv)
  app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
  myApp = MyApp()
  #myApp.show()

  try:
    sys.exit(app.exec_())
  except SystemExit:
    print('Closing Window...')










