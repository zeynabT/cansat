
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
            config.Battery -= 1
        # Discription label for UV & air quality
        self.airLabel = self.findChild(QLabel, "label_101")
        self.label_101.setFont(QFont('Arial', 10))
        if config.AirQuality < 17:
            self.airLabel.setText("Very Good")
        elif config.AirQuality < 33:
            self.airLabel.setText("Good")
        elif config.AirQuality < 49:
            self.airLabel.setText("Fair")
        elif config.AirQuality < 65:
            self.airLabel.setText("Poor")
        elif config.AirQuality < 81:
            self.airLabel.setText("Very Poor")
        elif config.AirQuality < 101:
            self.airLabel.setText("Hazardous")

        UVIndexValue = int(config.UVIndex)
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

        self.LA_angularX = self.findChild(QLabel, "label_96")
        self.LA_angularX.setText(str(config.A_angularX))
        self.LA_angularY = self.findChild(QLabel, "label_108")
        self.LA_angularY.setText(str(config.A_angularY))
        self.LA_angularZ = self.findChild(QLabel, "label_121")
        self.LA_angularZ.setText(str(config.A_angularZ))

        self.LA_linearX = self.findChild(QLabel, "label_97")
        self.LA_linearX.setText(str(config.A_linearX))
        self.LA_linearY = self.findChild(QLabel, "label_123")
        self.LA_linearY.setText(str(config.A_linearY))
        self.LA_linearZ = self.findChild(QLabel, "label_124")
        self.LA_linearZ.setText(str(config.A_linearZ))

        self.LAirQuality = self.findChild(QLabel, "label_52")
        self.LAirQuality.setText(str(config.AirQuality))

        self.LUVIndex = self.findChild(QLabel, "label_100")
        self.LUVIndex.setText(str(config.UVIndex))

        self.LCoordinate_x = self.findChild(QLabel, "label_103")
        self.LCoordinate_x.setText(str(config.CoordinateX))
        self.LCoordinate_y = self.findChild(QLabel, "label_105")
        self.LCoordinate_y.setText(str(config.CoordinateY))

        self.LPressure = self.findChild(QLabel, "label_2")
        self.LPressure.setText(str(config.Pressure))
        self.LPressure_1 = self.findChild(QLabel, "label_67")
        self.LPressure_1.setText(str(config.Pressure_1))
        self.LPressure_2 = self.findChild(QLabel, "label_69")
        self.LPressure_2.setText(str(config.Pressure_2))
        self.LPressure_3 = self.findChild(QLabel, "label_71")
        self.LPressure_3.setText(str(config.Pressure_3))
        self.LPressure_4 = self.findChild(QLabel, "label_73")
        self.LPressure_4.setText(str(config.Pressure_4))
        self.LPressure_5 = self.findChild(QLabel, "label_75")
        self.LPressure_5.setText(str(config.Pressure_5))
        self.LPressure_6 = self.findChild(QLabel, "label_77")
        self.LPressure_6.setText(str(config.Pressure_6))

        self.LInTemp_6 = self.findChild(QLabel, "label_35")
        self.LInTemp_6.setText(str(config.InTemp_6))
        self.LInTemp = self.findChild(QLabel, "label")
        self.LInTemp.setText(str(config.InTemp))
        self.LInTemp_1 = self.findChild(QLabel, "label_25")
        self.LInTemp_1.setText(str(config.InTemp_1))
        self.LInTemp_2 = self.findChild(QLabel, "label_27")
        self.LInTemp_2.setText(str(config.InTemp_2))
        self.LInTemp_3 = self.findChild(QLabel, "label_29")
        self.LInTemp_3.setText(str(config.InTemp_3))
        self.LInTemp_4 = self.findChild(QLabel, "label_31")
        self.LInTemp_4.setText(str(config.InTemp_4))
        self.LInTemp_5 = self.findChild(QLabel, "label_33")
        self.LInTemp_5.setText(str(config.InTemp_5))

        self.LOutTemp = self.findChild(QLabel, "label_37")
        self.LOutTemp.setText(str(config.OutTemp))
        self.LOutTemp_1 = self.findChild(QLabel, "label_39")
        self.LOutTemp_1.setText(str(config.OutTemp_1))
        self.LOutTemp_2 = self.findChild(QLabel, "label_41")
        self.LOutTemp_2.setText(str(config.OutTemp_2))
        self.LOutTemp_3 = self.findChild(QLabel, "label_43")
        self.LOutTemp_3.setText(str(config.OutTemp_3))
        self.LOutTemp_4 = self.findChild(QLabel, "label_45")
        self.LOutTemp_4.setText(str(config.OutTemp_4))
        self.LOutTemp_5 = self.findChild(QLabel, "label_47")
        self.LOutTemp_5.setText(str(config.OutTemp_5))
        self.LOutTemp_6 = self.findChild(QLabel, "label_49")
        self.LOutTemp_6.setText(str(config.OutTemp_6))

        self.LHiumidity = self.findChild(QLabel, "label_50")
        self.LHiumidity.setText(str(config.Hiumidity))
        self.LHiumidity_1 = self.findChild(QLabel, "label_54")
        self.LHiumidity_1.setText(str(config.Hiumidity_1))
        self.LHiumidity_2 = self.findChild(QLabel, "label_56")
        self.LHiumidity_2.setText(str(config.Hiumidity_2))
        self.LHiumidity_3 = self.findChild(QLabel, "label_58")
        self.LHiumidity_3.setText(str(config.Hiumidity_3))
        self.LHiumidity_4 = self.findChild(QLabel, "label_60")
        self.LHiumidity_4.setText(str(config.Hiumidity_4))
        self.LHiumidity_5 = self.findChild(QLabel, "label_62")
        self.LHiumidity_5.setText(str(config.Hiumidity_5))
        self.LHiumidity_6 = self.findChild(QLabel, "label_64")
        self.LHiumidity_6.setText(str(config.Hiumidity_6))

        self.graphWidget.plot(config.x_height, config.y_height)

        SPressure = self.findChild(QLabel, "label_110")
        if config.sensorPressure:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_111")
        if config.sensorAcceleration:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_112")
        if config.sensorTemp:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_114")
        if config.sensorHumidity:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_113")
        if config.sensorAirQ:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SPressure = self.findChild(QLabel, "label_116")
        if config.sensorUV:
            SPressure.setPixmap(self.pixmapG)
        else:
            SPressure.setPixmap(self.pixmapR)

        SgroundStationConnection = self.findChild(QLabel, "label_117")
        if config.sensorAirQ:
            SgroundStationConnection.setPixmap(self.pixmapG)
        else:
            SgroundStationConnection.setPixmap(self.pixmapR)

        SsatelliteConnection = self.findChild(QLabel, "label_118")
        if config.sensorAirQ:
            SsatelliteConnection.setPixmap(self.pixmapG)
        else:
            SsatelliteConnection.setPixmap(self.pixmapR)

        # # Map
        # m = folium.Map(
        #     tiles='OpenStreetMap',
        #     zoom_start=21,
        #     location=(36.318532, 59.525929),
        #     width=321,
        #     height=161
        # )
        # folium.Marker(
        #     location=[36.318532, 59.525929],
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
        if config.dataOfCamera == False:
            self.alarmText.setText(
                "warinig: Ground station can not receive any data from camera")
        self.alarmText.setText('info: '+config.log)
