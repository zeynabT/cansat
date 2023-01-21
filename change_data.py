
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
