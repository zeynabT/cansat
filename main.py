from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
import sys
import pyqtgraph as pg
import os
import io
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from threading import Thread
import threading
from worker import long_running_function, ProgressWorker
from change_data import get_data

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def sound():

    filename = os.path.join(CURRENT_DIR, "sound/red_danger_alarm_2_2.mp3")
    app2 = QtCore.QCoreApplication(sys.argv)
    player = QtMultimedia.QMediaPlayer()
    url = QtCore.QUrl.fromLocalFile(filename)
    player.setMedia(QtMultimedia.QMediaContent(url))
    player.play()

    sys.exit(app2.exec_())


class Ui(QtWidgets.QMainWindow):

    CoordinateX = 36.31130898586006
    CoordinateY = 59.526375931025
    Coordinate_x = str(CoordinateX)
    Coordinate_y = str(CoordinateY)
    coordinate = (CoordinateX, CoordinateY)

    pixmapG = ''
    pixmapR = ''

    def __init__(self, parent=None):
        super(Ui, self).__init__()
        uic.loadUi('CAN-SAT2.ui', self)
        # Good = "Good"
        # Low = "Low"
        # Moderate = "Moderate"
        # Heigh = "Heigh"
        # VeryHeigh = "Very Heigh"
        # Extreme = "Extreme"

        # alarm
        self.alarmText = self.findChild(QLabel, "label_109")
        self.label_109.setFont(QFont('Arial', 11))
        self.alarmText.setStyleSheet("color: rgb(175, 0,3)")

        self.alarm = self.findChild(QLabel, "label_108")
        self.label_108.setFont(QFont('Arial', 11))
        self.alarm.setStyleSheet("color: rgb(175, 0,3)")

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
        self.pixmapG = QPixmap('img/button-green.jpg')
        self.pixmapR = QPixmap('img/button-red.jpg')
        low_rez = QtCore.QSize(18, 18)
        self.pixmapG = self.pixmapG.scaled(low_rez)
        self.pixmapR = self.pixmapR.scaled(low_rez)

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
        # sound()

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

        # linearProgressbar
        self.progressBar_3.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        self.progressBar_4.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")
        self.progressBar_5.setStyleSheet(
            "border-radius: 7px;min-height: 20px;max-height: 20px;text-align: center")

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

        t = Thread(target=get_data, args=(self,))
        t.start()

        # height
        # height = MainWindow()
        self.graphWidget = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        temperature = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.graphWidget.setBackground('w')
        self.graphWidget.plot(hour, temperature)
        self.graphWidget.setGeometry(0, 0, 321, 191)

        self.graphWidget.setParent(self.findChild(QWidget, "widget_5"))
        self.launch()
        self.show()

    def launch(self):
        # progressBar_3
        worker_3 = ProgressWorker()
        worker_3.value_change.connect(self.progressBar_3.setValue)
        threading.Thread(
            target=long_running_function,
            args=("foo",),
            kwargs=dict(baz="baz", worker=worker_3),
            daemon=True,
        ).start()

        # progressBar_4
        worker_4 = ProgressWorker()
        worker_4.value_change.connect(self.progressBar_4.setValue)
        threading.Thread(
            target=long_running_function,
            args=("foo",),
            kwargs=dict(baz="baz", worker=worker_4),
            daemon=True,
        ).start()

        # progressBar_5
        worker_5 = ProgressWorker()
        worker_5.value_change.connect(self.progressBar_5.setValue)
        threading.Thread(
            target=long_running_function,
            args=("foo",),
            kwargs=dict(baz="baz", worker=worker_5),
            daemon=True,
        ).start()


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
    ui = Ui()
    app.exec_()
    # app.setStyleSheet('''
    #     QWidget {
    #         font-size: 35px;
    #     }
    # ''')

