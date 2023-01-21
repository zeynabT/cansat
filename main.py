from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
import io
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import time
from threading import Thread
import secrets
import sys
import threading
import os
from PyQt5 import QtCore, QtMultimedia
import time
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class PercentageWorker(QtCore.QObject):
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


def sound():

    filename = os.path.join(CURRENT_DIR, "sound/red_danger_alarm_2_2.mp3")
    app2 = QtCore.QCoreApplication(sys.argv)
    player = QtMultimedia.QMediaPlayer()
    url = QtCore.QUrl.fromLocalFile(filename)
    player.setMedia(QtMultimedia.QMediaContent(url))
    player.play()

    sys.exit(app2.exec_())


class Ui(QtWidgets.QMainWindow):
    A_angular = "12"
    A_linear = "20"
    Pressure = "60"
    Pressure_1 = "0"
    Pressure_2 = "0"
    Pressure_3 = "0"
    Pressure_4 = "0"
    Pressure_5 = "0"
    Pressure_6 = "0"

    InTemp = "2"
    InTemp_1 = "0"
    InTemp_2 = "0"
    InTemp_3 = "0"
    InTemp_4 = "0"
    InTemp_5 = "0"
    InTemp_6 = "0"

    OutTemp = "3"
    OutTemp_1 = "0"
    OutTemp_2 = "0"
    OutTemp_3 = "0"
    OutTemp_4 = "0"
    OutTemp_5 = "0"
    OutTemp_6 = "0"

    Hiumidity = "7"
    Hiumidity_1 = "0"
    Hiumidity_2 = "0"
    Hiumidity_3 = "0"
    Hiumidity_4 = "0"
    Hiumidity_5 = "0"
    Hiumidity_6 = "0"

    AirQuality = "4"
    UVIndex = "6"

    CoordinateX = 36.31130898586006
    CoordinateY = 59.526375931025
    Coordinate_x = str(CoordinateX)
    Coordinate_y = str(CoordinateY)
    coordinate = (CoordinateX, CoordinateY)

    sensorPressure = False
    sensorAcceleration = False
    sensorTemp = False
    sensorHumidity = False
    sensorAirQ = False
    sensorUV = False
    groundStationConnection = False
    satelliteConnection = False
    dataOfCamera = False

    def __init__(self, parent=None):
        super(Ui, self).__init__()
        uic.loadUi('CAN-SAT2.ui', self)

        Good = "Good"
        Low = "Low"
        Moderate = "Moderate"
        Heigh = "Heigh"
        VeryHeigh = "Very Heigh"
        Extreme = "Extreme"

        # setting label for every int
        self.LA_angular = self.findChild(QLabel, "label_96")
        self.LA_angular.setText(self.A_angular)
        self.LA_linear = self.findChild(QLabel, "label_97")
        self.LA_linear.setText(self.A_linear)
        self.LPressure = self.findChild(QLabel, "label_2")
        self.LPressure.setText(self.Pressure)
        self.LPressure_1 = self.findChild(QLabel, "label_67")
        self.LPressure_1.setText(self.Pressure_1)
        self.LPressure_2 = self.findChild(QLabel, "label_69")
        self.LPressure_2.setText(self.Pressure_2)
        self.LPressure_3 = self.findChild(QLabel, "label_71")
        self.LPressure_3.setText(self.Pressure_3)
        self.LPressure_4 = self.findChild(QLabel, "label_73")
        self.LPressure_4.setText(self.Pressure_4)
        self.LPressure_5 = self.findChild(QLabel, "label_75")
        self.LPressure_5.setText(self.Pressure_5)
        self.LPressure_6 = self.findChild(QLabel, "label_77")
        self.LPressure_6.setText(self.Pressure_6)

        self.LInTemp = self.findChild(QLabel, "label")
        self.LInTemp.setText(self.InTemp)
        self.LInTemp_1 = self.findChild(QLabel, "label_25")
        self.LInTemp_1.setText(self.InTemp_1)
        self.LInTemp_2 = self.findChild(QLabel, "label_27")
        self.LInTemp_2.setText(self.InTemp_2)
        self.LInTemp_3 = self.findChild(QLabel, "label_29")
        self.LInTemp_3.setText(self.InTemp_3)
        self.LInTemp_4 = self.findChild(QLabel, "label_31")
        self.LInTemp_4.setText(self.InTemp_4)
        self.LInTemp_5 = self.findChild(QLabel, "label_33")
        self.LInTemp_5.setText(self.InTemp_5)
        self.LInTemp_6 = self.findChild(QLabel, "label_35")
        self.LInTemp_6.setText(self.InTemp_6)

        self.LOutTemp = self.findChild(QLabel, "label_37")
        self.LOutTemp.setText(self.OutTemp)
        self.LOutTemp_1 = self.findChild(QLabel, "label_39")
        self.LOutTemp_1.setText(self.OutTemp_1)
        self.LOutTemp_2 = self.findChild(QLabel, "label_41")
        self.LOutTemp_2.setText(self.OutTemp_2)
        self.LOutTemp_3 = self.findChild(QLabel, "label_43")
        self.LOutTemp_3.setText(self.OutTemp_3)
        self.LOutTemp_4 = self.findChild(QLabel, "label_45")
        self.LOutTemp_4.setText(self.OutTemp_4)
        self.LOutTemp_5 = self.findChild(QLabel, "label_47")
        self.LOutTemp_5.setText(self.OutTemp_5)
        self.LOutTemp_6 = self.findChild(QLabel, "label_49")
        self.LOutTemp_6.setText(self.OutTemp_6)

        self.LHiumidity = self.findChild(QLabel, "label_50")
        self.LHiumidity.setText(self.Hiumidity)
        self.LHiumidity_1 = self.findChild(QLabel, "label_54")
        self.LHiumidity_1.setText(self.Hiumidity_1)
        self.LHiumidity_2 = self.findChild(QLabel, "label_56")
        self.LHiumidity_2.setText(self.Hiumidity_2)
        self.LHiumidity_3 = self.findChild(QLabel, "label_58")
        self.LHiumidity_3.setText(self.Hiumidity_3)
        self.LHiumidity_4 = self.findChild(QLabel, "label_60")
        self.LHiumidity_4.setText(self.Hiumidity_4)
        self.LHiumidity_5 = self.findChild(QLabel, "label_62")
        self.LHiumidity_5.setText(self.Hiumidity_5)
        self.LHiumidity_6 = self.findChild(QLabel, "label_64")
        self.LHiumidity_6.setText(self.Hiumidity_6)

        # alarm
        self.alarmText = self.findChild(QLabel, "label_109")
        self.label_109.setFont(QFont('Arial', 11))
        self.alarmText.setStyleSheet("color: rgb(175, 0,3)")

        self.alarm = self.findChild(QLabel, "label_108")
        self.label_108.setFont(QFont('Arial', 11))
        self.alarm.setStyleSheet("color: rgb(175, 0,3)")

        self.LAirQuality = self.findChild(QLabel, "label_52")
        self.LAirQuality.setText(self.AirQuality)

        self.LUVIndex = self.findChild(QLabel, "label_100")
        self.LUVIndex.setText(self.UVIndex)

        self.Coordinate_x = self.findChild(QLabel, "label_103")
        self.Coordinate_x.setText(str(self.CoordinateX))
        self.Coordinate_y = self.findChild(QLabel, "label_105")
        self.Coordinate_y.setText(str(self.CoordinateY))

        self.airLabel = self.findChild(QLabel, "label_101")
        self.label_101.setFont(QFont('Arial', 10))

        self.UVLabel = self.findChild(QLabel, "label_102")
        self.label_102.setFont(QFont('Arial', 10))
        self.iconText = self.setWindowTitle("FUM_CAN")
        self.windowIcon = self.setWindowIcon(QtGui.QIcon('img/logo-white.jpg'))

        # icon
        IPressure = self.findChild(QLabel, "label_5")
        pixmap = QPixmap('img/pressure.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IPressure.setPixmap(pixmap)

        IAcceleration = self.findChild(QLabel, "label_6")
        pixmap = QPixmap('img/Acceleration.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IAcceleration.setPixmap(pixmap)

        IInTemp = self.findChild(QLabel, "label_7")
        pixmap = QPixmap('img/icons8-temperature-inside2.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IInTemp.setPixmap(pixmap)

        IIOutTemp = self.findChild(QLabel, "label_8")
        pixmap = QPixmap('img/temperature-outside4.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        IIOutTemp.setPixmap(pixmap)

        IHiumidity = self.findChild(QLabel, "label_9")
        pixmap = QPixmap('img/humidity-.jpg')
        pixmap = pixmap.scaled(low_rez)
        IHiumidity.setPixmap(pixmap)

        IAirQuality = self.findChild(QLabel, "label_10")
        pixmap = QPixmap('img/wind2.jpg')
        pixmap = pixmap.scaled(low_rez)
        IAirQuality.setPixmap(pixmap)

        IUVIndex = self.findChild(QLabel, "label_11")
        pixmap = QPixmap('img/sun.jpg')
        pixmap = pixmap.scaled(low_rez)
        IUVIndex.setPixmap(pixmap)

        ISensor = self.findChild(QLabel, "label_12")
        pixmap = QPixmap('img/sensor.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor.setPixmap(pixmap)

        ISensor_pressure = self.findChild(QLabel, "label_78")
        pixmap = QPixmap('img/pressure.jpg')
        low_rez = QtCore.QSize(25, 25)
        pixmap = pixmap.scaled(low_rez)
        ISensor_pressure.setPixmap(pixmap)

        ISensor_acceleration = self.findChild(QLabel, "label_82")
        pixmap = QPixmap('img/Acceleration.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_acceleration.setPixmap(pixmap)

        ISensor_temp = self.findChild(QLabel, "label_84")
        pixmap = QPixmap('img/icons8-temperature-inside2.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_temp.setPixmap(pixmap)

        ISensor_hiumidity = self.findChild(QLabel, "label_79")
        pixmap = QPixmap('img/humidity-.jpg')
        low_rez = QtCore.QSize(23, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_hiumidity.setPixmap(pixmap)

        ISensor_air = self.findChild(QLabel, "label_83")
        pixmap = QPixmap('img/wind2.jpg')
        low_rez = QtCore.QSize(21, 21)
        pixmap = pixmap.scaled(low_rez)
        ISensor_air.setPixmap(pixmap)

        ISensor_UV = self.findChild(QLabel, "label_85")
        pixmap = QPixmap('img/sun.jpg')
        low_rez = QtCore.QSize(25, 23)
        pixmap = pixmap.scaled(low_rez)
        ISensor_UV.setPixmap(pixmap)

        ISatellite_1 = self.findChild(QLabel, "label_80")
        pixmap = QPixmap('img/satellite.jpg')
        low_rez = QtCore.QSize(23, 23)
        pixmap = pixmap.scaled(low_rez)
        ISatellite_1.setPixmap(pixmap)

        ISatellite_2 = self.findChild(QLabel, "label_81")
        pixmap = QPixmap('img/satellite.jpg')
        pixmap = pixmap.scaled(low_rez)
        ISatellite_2.setPixmap(pixmap)

        ILogo = self.findChild(QLabel, "label_107")
        pixmap = QPixmap('img/logo.jpg')
        low_rez = QtCore.QSize(50, 45)
        pixmap = pixmap.scaled(low_rez)
        ILogo.setPixmap(pixmap)

        receivedImage = QLabel()
        pixmap = QPixmap('img/image1.jpg')
        low_rez = QtCore.QSize(321, 200)
        pixmap = pixmap.scaled(low_rez)
        receivedImage.setPixmap(pixmap)
        imgWidget = self.findChild(QWidget, "widget_7")
        receivedImage.setParent(imgWidget)

        # Sensors
        pixmapG = QPixmap('img/button-green.jpg')
        pixmapR = QPixmap('img/button-red.jpg')
        low_rez = QtCore.QSize(18, 18)
        pixmapG = pixmapG.scaled(low_rez)
        pixmapR = pixmapR.scaled(low_rez)

        SPressure = self.findChild(QLabel, "label_110")
        if self.sensorPressure:
            SPressure.setPixmap(pixmapG)
        else:
            SPressure.setPixmap(pixmapR)

        SPressure = self.findChild(QLabel, "label_111")
        if self.sensorAcceleration:
            SPressure.setPixmap(pixmapG)
        else:
            SPressure.setPixmap(pixmapR)

        SPressure = self.findChild(QLabel, "label_112")
        if self.sensorTemp:
            SPressure.setPixmap(pixmapG)
        else:
            SPressure.setPixmap(pixmapR)
            
        SPressure = self.findChild(QLabel, "label_114")
        if self.sensorHumidity:
            SPressure.setPixmap(pixmapG)
        else:
            SPressure.setPixmap(pixmapR)

        SPressure = self.findChild(QLabel, "label_113")
        if self.sensorAirQ:
            SPressure.setPixmap(pixmapG)
        else:
            SPressure.setPixmap(pixmapR)

        SPressure = self.findChild(QLabel, "label_116")
        if self.sensorUV:
            SPressure.setPixmap(pixmapG)
        else:
            SPressure.setPixmap(pixmapR)

        SgroundStationConnection = self.findChild(QLabel, "label_117")
        if self.sensorAirQ:
            SgroundStationConnection.setPixmap(pixmapG)
        else:
            SgroundStationConnection.setPixmap(pixmapR)

        SsatelliteConnection = self.findChild(QLabel, "label_118")
        if self.sensorAirQ:
            SsatelliteConnection.setPixmap(pixmapG)
        else:
            SsatelliteConnection.setPixmap(pixmapR)
        
        # sound 
        filename = os.path.join(CURRENT_DIR, "sound/red_danger_alarm_2_2.mp3")
        # app2 = QtCore.QCoreApplication(sys.argv)
        player = QtMultimedia.QMediaPlayer()
        url = QtCore.QUrl.fromLocalFile(filename)
        player.setMedia(QtMultimedia.QMediaContent(url))
        # player.play()
        # time.sleep(2)
        # QtCore.QCoreApplication.quit()
        # sys.exit(app2.exec_())
        #sound()
        

        # Map
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=13,
            location=self.coordinate
        )
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        webView.setParent(self.findChild(QWidget, "widget_9"))
        webView.setStyleSheet("border-radius: 30px;")

        t = Thread(target=self.get_data)
        t2 = Thread(target=self.get_data2)
        t.start()
        t2.start()
       
        #linearProgressbar
        self.progressBar_3.setStyleSheet("border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        self.progressBar_4.setStyleSheet("border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        self.progressBar_5.setStyleSheet("border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        

        # linearProgressbar
        self.progressBar_3.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        self.progressBar_4.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        self.progressBar_5.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")

        # Battery
        self.progressBar_2.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")

        # height
        # height = MainWindow()
        self.graphWidget = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        temperature = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.graphWidget.setBackground('w')
        self.graphWidget.plot(hour, temperature)
        # vb = self.graphWidget.getViewBox()                                                           
        # vb.setAspectLocked(lock=False)                                                  
        # vb.setAutoVisible(y=0.5)                                                        
        # vb.enableAutoRange(axis='y', enable=True) 
        self.graphWidget.setGeometry(0, 0, 321, 191)
        # create list for y-axis
        # y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        
        # # create horizontal list i.e x-axis
        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # # create pyqt5graph bar graph item
        # # with width = 0.6
        # # with bar colors = green
        # bargraph1 = pg.BarGraphItem(x = x, height = y1, width = 0.6, brush ='g')
        
        # add item to plot window
        # adding bargraph item to the window
        # self.graphWidget.addItem(bargraph1)
        # 321, 161
        self.graphWidget.setParent(self.findChild(QWidget, "widget_5"))
        self.launch()
        self.show()

        ''' #roundProgressBar
        c = QtWidgets.QWidget()
        #CLASS INSTANCE
        c.rpb = roundProgressBar()
        #LINE WIDTH 
        c.rpb.rpb_setLineWidth(10)
        #LINE CAP
        c.rpb.rpb_setLineCap('RoundCap')
        c.rpb.rpb_setValue(45)
        '''

    def launch(self):
        worker = PercentageWorker()
        worker.percentageChanged.connect(self.progressBar_4.setValue)
        threading.Thread(
            target=long_running_function,
            args=("foo",),
            kwargs=dict(baz="baz", worker=worker),
            daemon=True,
        ).start()

    def get_data2(self):  
        
        for i in range(200):  
            time.sleep(1) 

    def get_data(self):

        for i in range(200):
            time.sleep(1)

            self.A_angular = str(secrets.randbelow(100))
            self.A_linear = str(secrets.randbelow(100))
            if i == 5 :
                            
                # filename = os.path.join(CURRENT_DIR, "sound/red_danger_alarm_2_2.mp3")
                # app2 = QtCore.QCoreApplication(sys.argv)
                # player = QtMultimedia.QMediaPlayer()
                # url = QtCore.QUrl.fromLocalFile(filename)
                # player.setMedia(QtMultimedia.QMediaContent(url))
                # player.play()
                # sys.exit(app2.exec_())
                self.t2.quit()

    
    def get_data(self):  
        
        for i in range(200):  
            time.sleep(1) 
            # self.A_angular = str(secrets.randbelow(100))
            # self.A_linear = str(secrets.randbelow(100))

            # Discription label for UV & air quality
            AirQualityValue = secrets.randbelow(100)
            self.AirQuality = str(AirQualityValue)
            self.airLabel = self.findChild(QLabel, "label_101")
            self.label_101.setFont(QFont('Arial', 10))
            if AirQualityValue < 17:
                self.airLabel.setText("Very Good")
            elif AirQualityValue < 33:
                self.airLabel.setText("Good")
            elif AirQualityValue < 49:
                self.airLabel.setText("Fair")
            elif AirQualityValue < 65:
                self.airLabel.setText("Poor")
            elif AirQualityValue < 81:
                self.airLabel.setText("Very Poor")
            elif AirQualityValue < 101:
                self.airLabel.setText("Hazardous")

            self.alarmText = self.findChild(QLabel, "label_109")
            self.alarm = self.findChild(QLabel, "label_108")
            if self.dataOfCamera == False:
                self.alarmText.setText(
                    "Ground station can not receive any data from camera")
                self.alarm.setText("Alarm:")

            UVIndexValue = secrets.randbelow(100)
            self.UVIndex = str(UVIndexValue)
            self.UVLabel = self.findChild(QLabel, "label_102")
            self.label_102.setFont(QFont("Arial [red]", 10))

            if UVIndexValue < 17:
                self.UVLabel.setText("Very Good")
            elif UVIndexValue < 33:
                self.UVLabel.setText("Good")
            elif UVIndexValue < 49:
                self.UVLabel.setText("Fair")
            elif UVIndexValue < 65:
                self.UVLabel.setText("Poor")
            elif UVIndexValue < 81:
                self.UVLabel.setText("Very Poor")
            elif UVIndexValue < 101:
                self.UVLabel.setText("Hazardous")

            self.CoordinateX = 36.31130898586006
            self.CoordinateY = 59.526375931025
            self.Coordinate_x = str(self.CoordinateX)
            self.Coordinate_y = str(self.CoordinateY)
            self.coordinate = (self.CoordinateX, self.CoordinateY)

            self.LA_angular = self.findChild(QLabel, "label_96")
            self.LA_angular.setText(self.A_angular)
            self.LA_linear = self.findChild(QLabel, "label_97")
            self.LA_linear.setText(self.A_linear)

            self.LAirQuality = self.findChild(QLabel, "label_52")
            self.LAirQuality.setText(self.AirQuality)

            self.LUVIndex = self.findChild(QLabel, "label_100")
            self.LUVIndex.setText(self.UVIndex)

            self.LCoordinate_x = self.findChild(QLabel, "label_103")
            self.LCoordinate_x.setText(self.Coordinate_x)
            self.LCoordinate_y = self.findChild(QLabel, "label_105")
            self.LCoordinate_y.setText(self.Coordinate_y)

            self.Pressure_6 = self.Pressure_5
            self.Pressure_5 = self.Pressure_4
            self.Pressure_4 = self.Pressure_3
            self.Pressure_3 = self.Pressure_2
            self.Pressure_2 = self.Pressure_1
            self.Pressure_1 = self.Pressure
            self.Pressure = str(secrets.randbelow(100))

            self.InTemp_6 = self.InTemp_5
            self.InTemp_5 = self.InTemp_4
            self.InTemp_4 = self.InTemp_3
            self.InTemp_3 = self.InTemp_2
            self.InTemp_2 = self.InTemp_1
            self.InTemp_1 = self.InTemp
            self.InTemp = str(secrets.randbelow(100))

            self.OutTemp_6 = self.OutTemp_5
            self.OutTemp_5 = self.OutTemp_4
            self.OutTemp_4 = self.OutTemp_3
            self.OutTemp_3 = self.OutTemp_2
            self.OutTemp_2 = self.OutTemp_1
            self.OutTemp_1 = self.OutTemp
            self.OutTemp = str(secrets.randbelow(100))

            self.Hiumidity_6 = self.Hiumidity_5
            self.Hiumidity_5 = self.Hiumidity_4
            self.Hiumidity_4 = self.Hiumidity_3
            self.Hiumidity_3 = self.Hiumidity_2
            self.Hiumidity_2 = self.Hiumidity_1
            self.Hiumidity_1 = self.Hiumidity
            self.Hiumidity = str(secrets.randbelow(100))

            self.LPressure = self.findChild(QLabel, "label_2")
            self.LPressure.setText(self.Pressure)
            self.LPressure_1 = self.findChild(QLabel, "label_67")
            self.LPressure_1.setText(self.Pressure_1)
            self.LPressure_2 = self.findChild(QLabel, "label_69")
            self.LPressure_2.setText(self.Pressure_2)
            self.LPressure_3 = self.findChild(QLabel, "label_71")
            self.LPressure_3.setText(self.Pressure_3)
            self.LPressure_4 = self.findChild(QLabel, "label_73")
            self.LPressure_4.setText(self.Pressure_4)
            self.LPressure_5 = self.findChild(QLabel, "label_75")
            self.LPressure_5.setText(self.Pressure_5)
            self.LPressure_6 = self.findChild(QLabel, "label_77")
            self.LPressure_6.setText(self.Pressure_6)

            self.LInTemp_6 = self.findChild(QLabel, "label_35")
            self.LInTemp_6.setText(self.InTemp_6)
            self.LInTemp = self.findChild(QLabel, "label")
            self.LInTemp.setText(self.InTemp)
            self.LInTemp_1 = self.findChild(QLabel, "label_25")
            self.LInTemp_1.setText(self.InTemp_1)
            self.LInTemp_2 = self.findChild(QLabel, "label_27")
            self.LInTemp_2.setText(self.InTemp_2)
            self.LInTemp_3 = self.findChild(QLabel, "label_29")
            self.LInTemp_3.setText(self.InTemp_3)
            self.LInTemp_4 = self.findChild(QLabel, "label_31")
            self.LInTemp_4.setText(self.InTemp_4)
            self.LInTemp_5 = self.findChild(QLabel, "label_33")
            self.LInTemp_5.setText(self.InTemp_5)

            self.LOutTemp = self.findChild(QLabel, "label_37")
            self.LOutTemp.setText(self.OutTemp)
            self.LOutTemp_1 = self.findChild(QLabel, "label_39")
            self.LOutTemp_1.setText(self.OutTemp_1)
            self.LOutTemp_2 = self.findChild(QLabel, "label_41")
            self.LOutTemp_2.setText(self.OutTemp_2)
            self.LOutTemp_3 = self.findChild(QLabel, "label_43")
            self.LOutTemp_3.setText(self.OutTemp_3)
            self.LOutTemp_4 = self.findChild(QLabel, "label_45")
            self.LOutTemp_4.setText(self.OutTemp_4)
            self.LOutTemp_5 = self.findChild(QLabel, "label_47")
            self.LOutTemp_5.setText(self.OutTemp_5)
            self.LOutTemp_6 = self.findChild(QLabel, "label_49")
            self.LOutTemp_6.setText(self.OutTemp_6)

            self.LHiumidity = self.findChild(QLabel, "label_50")
            self.LHiumidity.setText(self.Hiumidity)
            self.LHiumidity_1 = self.findChild(QLabel, "label_54")
            self.LHiumidity_1.setText(self.Hiumidity_1)
            self.LHiumidity_2 = self.findChild(QLabel, "label_56")
            self.LHiumidity_2.setText(self.Hiumidity_2)
            self.LHiumidity_3 = self.findChild(QLabel, "label_58")
            self.LHiumidity_3.setText(self.Hiumidity_3)
            self.LHiumidity_4 = self.findChild(QLabel, "label_60")
            self.LHiumidity_4.setText(self.Hiumidity_4)
            self.LHiumidity_5 = self.findChild(QLabel, "label_62")
            self.LHiumidity_5.setText(self.Hiumidity_5)
            self.LHiumidity_6 = self.findChild(QLabel, "label_64")
            self.LHiumidity_6.setText(self.Hiumidity_6)

        # self.graphWidget = pg.PlotWidget()
        # hour = [1,2,3,4,5,6,7,8,9,10]
        # temperature = [1,2,3,4,5,1,2,3,4,5]

        # self.graphWidget.setBackground('w')
        # self.graphWidget.plot(hour, temperature)

        # self.graphWidget.scale(100,100)
        # a = self.findChild(QWidget, "widget_5")
        # a.addWidget(self.graphWidget)
        # self.graphWidget.setParent(self.findChild(QWidget, "widget_5"))


# map
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

# height
# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         self.graphWidget = pg.PlotWidget()
#         #self.setCentralWidget(self.graphWidget)
#         self.graphWidget.scale(321, 161)
#         hour = [1,2,3,4,5,6,7,8,9]
#         temperature = [1,2,3,4,5,6,7,8,9]
#         self.graphWidget.setBackground('w')
#         self.graphWidget.plot(hour, temperature)

# progressBar


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        # CLASS INSTANCE
        self.rpb = roundProgressBar()
        # LINE WIDTH
        self.rpb.rpb_setLineWidth(10)
        # LINE CAP
        self.rpb.rpb_setLineCap('RoundCap')
        self.rpb.rpb_setValue(45)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui=Ui()
    app.exec_()
    # app.setStyleSheet('''
    #     QWidget {
    #         font-size: 35px;
    #     }
    # ''')

#   myApp = MyApp()

#   #myApp.show()

#   try:
#     sys.exit(app.exec_())
#   except SystemExit:
#     print('Closing Window...')

