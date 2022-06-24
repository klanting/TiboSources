from PyQt5 import QtCore, QtGui, QtWidgets

class GUI:
    def __init__(self, data):
        self.mapping = []
        self.scale = 2

        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(0, 0, len(data)*140*self.scale, 540)
        #MainWindow.resize(len(data)*140*self.scale, 540)
        _translate = QtCore.QCoreApplication.translate

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, len(data)*140, 270))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Weather_overview_colomn = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Weather_overview_colomn.setContentsMargins(0, 0, 0, 0)
        self.Weather_overview_colomn.setObjectName("Weather_overview_colomn")

        """here setup weather"""
        for i, tup in enumerate(data):
            box = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
            box.setObjectName(f"weather_{i}")

            day = QtWidgets.QLabel(box)
            day.setGeometry(QtCore.QRect(10, 10, 120, 40))
            font = QtGui.QFont()
            font.setPointSize(10*self.scale)
            day.setFont(font)
            day.setStyleSheet("QLabel{text-align: center;}")
            day.setAlignment(QtCore.Qt.AlignCenter)
            day.setObjectName(f"day_{i}")

            cloud_img = QtWidgets.QGraphicsView(box)
            cloud_img.setGeometry(QtCore.QRect(30, 60, 70, 60))
            cloud_img.setObjectName("cloud_today")

            temp = QtWidgets.QLabel(box)
            temp.setGeometry(QtCore.QRect(10, 130, 120, 40))
            font = QtGui.QFont()
            font.setPointSize(10*self.scale)
            temp.setFont(font)
            temp.setAlignment(QtCore.Qt.AlignCenter)
            temp.setObjectName(f"temp_{i}")

            rain_chance = QtWidgets.QLabel(box)
            rain_chance.setGeometry(QtCore.QRect(10, 190, 120, 30))
            font = QtGui.QFont()
            font.setPointSize(10*self.scale)
            rain_chance.setFont(font)
            rain_chance.setAlignment(QtCore.Qt.AlignCenter)
            rain_chance.setObjectName(f"rain_chance_{i}")

            day.setText(_translate("MainWindow", tup[0]))
            temp.setText(_translate("MainWindow", f"{tup[1]}/{tup[2]}"))
            rain_chance.setText(_translate("MainWindow", tup[3]))

            self.mapping.append((box, day, cloud_img, temp, rain_chance))

            self.Weather_overview_colomn.addWidget(box)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 22))
        self.menubar.setObjectName("menubar")
        self.menuoverview = QtWidgets.QMenu(self.menubar)
        self.menuoverview.setObjectName("menuoverview")
        self.menuweather = QtWidgets.QMenu(self.menubar)
        self.menuweather.setObjectName("menuweather")
        self.menustocks = QtWidgets.QMenu(self.menubar)
        self.menustocks.setObjectName("menustocks")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuoverview.menuAction())
        self.menubar.addAction(self.menuweather.menuAction())
        self.menubar.addAction(self.menustocks.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.menuoverview.setTitle(_translate("MainWindow", "overview"))
        self.menuweather.setTitle(_translate("MainWindow", "weather"))
        self.menustocks.setTitle(_translate("MainWindow", "stocks"))



if __name__ == "__main__":
    import sys, os
    app = QtWidgets.QApplication(sys.argv)

    screen = app.primaryScreen()
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    MainWindow = QtWidgets.QMainWindow()
    ui = GUI([('Tonight', '--', '8°', '7%', 'Mostly Cloudy'), ('Tue 31', '18°', '8°', '79%', 'PM Showers'), ('Wed 01', '18°', '8°', '22%', 'Partly Cloudy'), ('Thu 02', '22°', '11°', '12%', 'Partly Cloudy'), ('Fri 03', '24°', '12°', '19%', 'Partly Cloudy'), ('Sat 04', '21°', '11°', '43%', 'AM Showers'), ('Sun 05', '23°', '13°', '49%', 'Showers'), ('Mon 06', '21°', '13°', '34%', 'PM Showers')])
    MainWindow.show()
    print(MainWindow.x())
    sys.exit(app.exec_())