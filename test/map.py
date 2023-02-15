
# import the library
# https://www.python-graph-gallery.com/312-add-markers-on-folium-map
import folium
# Import the pandas library
import pandas as pd
import time
import threading


# Map   
m = folium.Map(
    tiles='OpenStreetMap',
    zoom_start=14,
    location=(36.308314, 59.529174),
    width=321,
    height=161
)
folium.Marker(
    location=[36.308314, 59.529174],
    popup='fumcan',
).add_to(m)
m.fit_bounds([[36.318532, 59.525929],[36.314229, 59.539871],[36.304747, 59.516192],[36.302157, 59.536633]])
# Show the map
m.show_in_browser()















# import sys
# import io
# import folium # pip install folium
# from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
# from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine

# """
# Folium in PyQt5
# """
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.window_width, self.window_height = 1000, 1000
#         self.setMinimumSize(self.window_width, self.window_height)

#         layout = QVBoxLayout()
#         self.setLayout(layout)

       
#         coordinate = (x, y)
        
#         m = folium.Map(
#         	tiles='Stamen Terrain',
#         	zoom_start=13,
#         	location=coordinate
#         )

#         # save map data to data object
#         data = io.BytesIO()
#         m.save(data, close_file=False)

#         webView = QWebEngineView()
#         webView.setHtml(data.getvalue().decode())
#         layout.addWidget(webView)
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyleSheet('''
#         QWidget {
#             font-size: 35px;
#         }
#     ''')
    
#     myApp = MyApp()
#     #myApp.show()

#     try:
#         sys.exit(app.exec_())
#     except SystemExit:
#         print('Closing Window...')