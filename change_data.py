
import time
import secrets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
import config 


def get_data(self):

    for i in range(200):
        time.sleep(1)

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

        config.Pressure_6 = config.Pressure_5
        config.Pressure_5 = config.Pressure_4
        config.Pressure_4 = config.Pressure_3
        config.Pressure_3 = config.Pressure_2
        config.Pressure_2 = config.Pressure_1
        config.Pressure_1 = config.Pressure
        config.Pressure = str(secrets.randbelow(100))

        config.InTemp_6 = config.InTemp_5
        config.InTemp_5 = config.InTemp_4
        config.InTemp_4 = config.InTemp_3
        config.InTemp_3 = config.InTemp_2
        config.InTemp_2 = config.InTemp_1
        config.InTemp_1 = config.InTemp
        config.InTemp = str(secrets.randbelow(100))

        config.OutTemp_6 = config.OutTemp_5
        config.OutTemp_5 = config.OutTemp_4
        config.OutTemp_4 = config.OutTemp_3
        config.OutTemp_3 = config.OutTemp_2
        config.OutTemp_2 = config.OutTemp_1
        config.OutTemp_1 = config.OutTemp
        config.OutTemp = str(secrets.randbelow(100))

        config.Hiumidity_6 = config.Hiumidity_5
        config.Hiumidity_5 = config.Hiumidity_4
        config.Hiumidity_4 = config.Hiumidity_3
        config.Hiumidity_3 = config.Hiumidity_2
        config.Hiumidity_2 = config.Hiumidity_1
        config.Hiumidity_1 = config.Hiumidity
        config.Hiumidity = str(secrets.randbelow(100))

        self.LPressure = self.findChild(QLabel, "label_2")
        self.LPressure.setText(config.Pressure)
        self.LPressure_1 = self.findChild(QLabel, "label_67")
        self.LPressure_1.setText(config.Pressure_1)
        self.LPressure_2 = self.findChild(QLabel, "label_69")
        self.LPressure_2.setText(config.Pressure_2)
        self.LPressure_3 = self.findChild(QLabel, "label_71")
        self.LPressure_3.setText(config.Pressure_3)
        self.LPressure_4 = self.findChild(QLabel, "label_73")
        self.LPressure_4.setText(config.Pressure_4)
        self.LPressure_5 = self.findChild(QLabel, "label_75")
        self.LPressure_5.setText(config.Pressure_5)
        self.LPressure_6 = self.findChild(QLabel, "label_77")
        self.LPressure_6.setText(config.Pressure_6)

        self.LInTemp_6 = self.findChild(QLabel, "label_35")
        self.LInTemp_6.setText(config.InTemp_6)
        self.LInTemp = self.findChild(QLabel, "label")
        self.LInTemp.setText(config.InTemp)
        self.LInTemp_1 = self.findChild(QLabel, "label_25")
        self.LInTemp_1.setText(config.InTemp_1)
        self.LInTemp_2 = self.findChild(QLabel, "label_27")
        self.LInTemp_2.setText(config.InTemp_2)
        self.LInTemp_3 = self.findChild(QLabel, "label_29")
        self.LInTemp_3.setText(config.InTemp_3)
        self.LInTemp_4 = self.findChild(QLabel, "label_31")
        self.LInTemp_4.setText(config.InTemp_4)
        self.LInTemp_5 = self.findChild(QLabel, "label_33")
        self.LInTemp_5.setText(config.InTemp_5)

        self.LOutTemp = self.findChild(QLabel, "label_37")
        self.LOutTemp.setText(config.OutTemp)
        self.LOutTemp_1 = self.findChild(QLabel, "label_39")
        self.LOutTemp_1.setText(config.OutTemp_1)
        self.LOutTemp_2 = self.findChild(QLabel, "label_41")
        self.LOutTemp_2.setText(config.OutTemp_2)
        self.LOutTemp_3 = self.findChild(QLabel, "label_43")
        self.LOutTemp_3.setText(config.OutTemp_3)
        self.LOutTemp_4 = self.findChild(QLabel, "label_45")
        self.LOutTemp_4.setText(config.OutTemp_4)
        self.LOutTemp_5 = self.findChild(QLabel, "label_47")
        self.LOutTemp_5.setText(config.OutTemp_5)
        self.LOutTemp_6 = self.findChild(QLabel, "label_49")
        self.LOutTemp_6.setText(config.OutTemp_6)

        self.LHiumidity = self.findChild(QLabel, "label_50")
        self.LHiumidity.setText(config.Hiumidity)
        self.LHiumidity_1 = self.findChild(QLabel, "label_54")
        self.LHiumidity_1.setText(config.Hiumidity_1)
        self.LHiumidity_2 = self.findChild(QLabel, "label_56")
        self.LHiumidity_2.setText(config.Hiumidity_2)
        self.LHiumidity_3 = self.findChild(QLabel, "label_58")
        self.LHiumidity_3.setText(config.Hiumidity_3)
        self.LHiumidity_4 = self.findChild(QLabel, "label_60")
        self.LHiumidity_4.setText(config.Hiumidity_4)
        self.LHiumidity_5 = self.findChild(QLabel, "label_62")
        self.LHiumidity_5.setText(config.Hiumidity_5)
        self.LHiumidity_6 = self.findChild(QLabel, "label_64")
        self.LHiumidity_6.setText(config.Hiumidity_6)
