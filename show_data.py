
import time
import secrets
from PyQt5.QtWidgets import QLabel,QWidget
from PyQt5.QtGui import QFont
import config


def show_data(self):

    for i in range(200):
        time.sleep(1)

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

        self.alarmText = self.findChild(QLabel, "label_109")
        self.alarm = self.findChild(QLabel, "label_108")
        if config.dataOfCamera == False:
            self.alarmText.setText(
                "Ground station can not receive any data from camera")
            self.alarm.setText("Alarm:")

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

        self.CoordinateX = self.CoordinateX+1
        self.CoordinateY = self.CoordinateY + 1
        self.Coordinate_x = str(self.CoordinateX)
        self.Coordinate_y = str(self.CoordinateY)
        self.coordinate = (self.CoordinateX, self.CoordinateY)

        self.LA_angular = self.findChild(QLabel, "label_96")
        self.LA_angular.setText(str(config.A_angular))
        self.LA_linear = self.findChild(QLabel, "label_97")
        self.LA_linear.setText(str(config.A_linear))

        self.LAirQuality = self.findChild(QLabel, "label_52")
        self.LAirQuality.setText(str(config.AirQuality))

        self.LUVIndex = self.findChild(QLabel, "label_100")
        self.LUVIndex.setText(str(config.UVIndex))

        self.LCoordinate_x = self.findChild(QLabel, "label_103")
        self.LCoordinate_x.setText(self.Coordinate_x)
        self.LCoordinate_y = self.findChild(QLabel, "label_105")
        self.LCoordinate_y.setText(self.Coordinate_y)


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
        # self.graphWidget.addItem(config.x_height, config.y_height)

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
