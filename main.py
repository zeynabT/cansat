from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QLabel, QApplication, QWidget
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
from show_data import show_data
from get_data import get_data_from_server
import config

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

    pixmapG = ''
    pixmapR = ''
    webView = ''

    def __init__(self, parent=None):
        super(Ui, self).__init__()
        uic.loadUi('CAN-SAT2.ui', self)

        Coordinate_x = self.findChild(QLabel, "label_103")
        Coordinate_x.setText(str(config.coordinate_x))
        Coordinate_y = self.findChild(QLabel, "label_105")
        Coordinate_y.setText(str(config.coordinate_y))

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
        pixmap = QPixmap('img/1.jpg')
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

        # height
        self.graphWidget = pg.PlotWidget()

        self.graphWidget.setBackground('w')
        self.graphWidget.plot(config.height_x, config.height_y)
        self.graphWidget.setGeometry(0, 0, 321, 191)
        self.graphWidget.setParent(self.findChild(QWidget, "widget_5"))

        # Map
        m = folium.Map(
            tiles='OpenStreetMap',
            zoom_start=21,
            location=(config.coordinate_x, config.coordinate_y),
            width=321,
            height=161
        )
        folium.Marker(
            location=[config.coordinate_x, config.coordinate_y],
            popup='fumcan',
        ).add_to(m)
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        self.webView.setStyleSheet("border-radius: 30px;")
        self.webView.setParent(self.findChild(QWidget, "widget_9"))

        get_data_t = Thread(target=get_data_from_server)
        get_data_t.start()

        t = Thread(target=show_data, args=(self,), daemon=True)
        t.start()

        self.launch()
        self.show()

    def launch(self):
        # progressBar_2
        worker_2 = ProgressWorker()
        worker_2.value_change.connect(self.progressBar_2.setValue)
        threading.Thread(
            target=long_running_function,
            args=("Battery",),
            kwargs=dict(baz="baz", worker=worker_2),
            daemon=True,
        ).start()

        # progressBar_3
        worker_3 = ProgressWorker()
        worker_3.value_change.connect(self.progressBar_3.setValue)
        threading.Thread(
            target=long_running_function,
            args=("Pressure",),
            kwargs=dict(baz="baz", worker=worker_3),
            daemon=True,
        ).start()

        # progressBar_4
        worker_4 = ProgressWorker()
        worker_4.value_change.connect(self.progressBar_4.setValue)
        threading.Thread(
            target=long_running_function,
            args=("AirQuality",),
            kwargs=dict(baz="baz", worker=worker_4),
            daemon=True,
        ).start()

        # progressBar_5
        worker_5 = ProgressWorker()
        worker_5.value_change.connect(self.progressBar_5.setValue)
        threading.Thread(
            target=long_running_function,
            args=("UVIndex",),
            kwargs=dict(baz="baz", worker=worker_5),
            daemon=True,
        ).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    app.exec_()
    print('GodBy')
