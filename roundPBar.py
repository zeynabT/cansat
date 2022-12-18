import sys
from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(80)
        self.progress.setStyleSheet("color: red;\n"
                                    "background-color: blue;\n"
                                    "selection-background-color: yellow;")
        self.progress.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(200, 80)
    widget.show()
    sys.exit(app.exec())