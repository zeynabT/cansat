import time
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QFont
import config
import folium
import io
from PyQt5.QtWebEngineWidgets import QWebEngineView


def show_data(self):

    for i in range(7200):
        time.sleep(1)
        if i % 72 == 0:
            config.battery -= 1
        # # Discription label for Humitidit**************
        # UVIndexValue = int(config.UVIndex)
        # self.UVLabel = self.findChild(QLabel, "label_102")
        # self.label_102.setFont(QFont("Arial [red]", 10))
        # if UVIndexValue < 17:
        #     self.UVLabel.setText("Very Good")
        # elif UVIndexValue < 33:
        #     self.UVLabel.setText("Good")
        # elif UVIndexValue < 49:
        #     self.UVLabel.setText("Fair")
        # elif UVIndexValue < 65:
        #     self.UVLabel.setText("Poor")
        # elif UVIndexValue < 81:
        #     self.UVLabel.setText("Very Poor")
        # elif UVIndexValue < 101:
        #     self.UVLabel.setText("Hazardous")

        self.LA_angularX = self.findChild(QLabel, "label_96")
        self.LA_angularX.setText(str(config.acceleration_angular_x))
        self.LA_angularY = self.findChild(QLabel, "label_108")
        self.LA_angularY.setText(str(config.acceleration_angular_y))
        self.LA_angularZ = self.findChild(QLabel, "label_121")
        self.LA_angularZ.setText(str(config.acceleration_angular_z))

        self.LA_linearX = self.findChild(QLabel, "label_97")
        self.LA_linearX.setText(str(config.acceleration_linear_x))
        self.LA_linearY = self.findChild(QLabel, "label_123")
        self.LA_linearY.setText(str(config.acceleration_linear_y))
        self.LA_linearZ = self.findChild(QLabel, "label_124")
        self.LA_linearZ.setText(str(config.acceleration_linear_z))

        # self.LUVIndex = self.findChild(QLabel, "label_100")
        # self.LUVIndex.setText(str(config.UVIndex))

        self.LCoordinate_x = self.findChild(QLabel, "label_103")
        self.LCoordinate_x.setText(str(config.coordinate_x))
        self.LCoordinate_y = self.findChild(QLabel, "label_105")
        self.LCoordinate_y.setText(str(config.coordinate_y))

        self.LPressure = self.findChild(QLabel, "label_2")
        self.LPressure.setText(str(config.pressure))
        self.LPressure_1 = self.findChild(QLabel, "label_67")
        self.LPressure_1.setText(str(config.pressure_1))
        self.LPressure_2 = self.findChild(QLabel, "label_69")
        self.LPressure_2.setText(str(config.pressure_2))
        self.LPressure_3 = self.findChild(QLabel, "label_71")
        self.LPressure_3.setText(str(config.pressure_3))
        self.LPressure_4 = self.findChild(QLabel, "label_73")
        self.LPressure_4.setText(str(config.pressure_4))
        self.LPressure_5 = self.findChild(QLabel, "label_75")
        self.LPressure_5.setText(str(config.pressure_5))
        self.LPressure_6 = self.findChild(QLabel, "label_77")
        self.LPressure_6.setText(str(config.pressure_6))

        self.label_39.setText(str(config.speed))
        self.label_25.setText(str(config.speed_1))
        self.label_27.setText(str(config.speed_2))
        self.label_29.setText(str(config.speed_3))
        self.label_31.setText(str(config.speed_4))
        self.label_33.setText(str(config.speed_5))
        self.label_35.setText(str(config.speed_6))

        self.LInTemp = self.findChild(QLabel, "label")
        self.LInTemp.setText(str(config.in_temp))

        self.LOutTemp = self.findChild(QLabel, "label_37")
        self.LOutTemp.setText(str(config.out_temp))

        self.LHiumidity = self.findChild(QLabel, "label_100")
        self.LHiumidity.setText(str(config.hiumidity))

        self.label_128.setText(config.sunlight_visible)
        self.label_130.setText(config.sunlight_infrared)
        self.label_131.setText(config.sunlight_spectrum)

        self.graphWidget.plot(config.height_x, config.height_y)

        SPressure = self.findChild(QLabel, "label_110")
        if config.sensor_pressure:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_111")
        if config.sensor_acceleration:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_112")
        if config.sensor_temp:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_114")
        if config.sensor_humidity:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_113")
        if config.sensor_gsm:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_116")
        if config.sensor_sunlight:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        # # Map
        # m = folium.Map(
        #     tiles='OpenStreetMap',
        #     zoom_start=21,
        #     location=(config.CoordinateX, config.CoordinateY),
        #     width=321,
        #     height=161
        # )
        # folium.Marker(
        #     location=[config.CoordinateX, config.CoordinateY],
        #     popup='fumcan',
        # ).add_to(m)
        # # save map data to data object
        # data = io.BytesIO()
        # m.save(data, close_file=False)

        # self.webView = QWebEngineView()
        # self.webView.setHtml(data.getvalue().decode())
        # self.webView.setStyleSheet("border-radius: 30px;")
        # self.webView.setParent(self.findChild(QWidget, "widget_9"))

        # log
        self.alarmText = self.findChild(QLabel, "label_109")
        if config.data_Of_Camera == False:
            self.alarmText.setText(
                "warinig: Ground station can not receive any data from camera")
        self.alarmText.setText('info: '+config.log)
