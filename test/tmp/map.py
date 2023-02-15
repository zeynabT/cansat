# map
# class MyApp(QWidget):
#     def __init__(self, webveiw):
#         self.webview = webveiw
#         super().__init__()
#         self.setWindowTitle('Map')
#         self.window_width, self.window_height = 1000, 1000
#         self.setMinimumSize(self.window_width, self.window_height)

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         x = 37.8199286
#         y = -122.4782551
#         coordinate = (x, y)

#         m = folium.Map(
#             tiles='Stamen Terrain',
#             zoom_start=13,
#             location=coordinate
#         )

#         # save map data to data object
#         data = io.BytesIO()
#         m.save(data, close_file=False)

#         webview = QWebEngineView()
#         webview.setHtml(data.getvalue().decode())
#         layout.addWidget(webview)
#         self.show()


# progressBar
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)

#         # CLASS INSTANCE
#         self.rpb = roundProgressBar()
#         # LINE WIDTH
#         self.rpb.rpb_setLineWidth(10)
#         # LINE CAP
#         self.rpb.rpb_setLineCap('RoundCap')
#         self.rpb.rpb_setValue(45)

#         self.layout = QtWidgets.QHBoxLayout()
#         self.layout.addWidget(self.rpb)
#         self.setLayout(self.layout)