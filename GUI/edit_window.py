# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 81, 16))
        self.label.setObjectName("label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(100, 60, 221, 16))
        self.name_label.setObjectName("name_label")
        self.year_label = QtWidgets.QLabel(self.centralwidget)
        self.year_label.setGeometry(QtCore.QRect(100, 110, 221, 16))
        self.year_label.setObjectName("year_label")
        self.month_label = QtWidgets.QLabel(self.centralwidget)
        self.month_label.setGeometry(QtCore.QRect(100, 160, 221, 16))
        self.month_label.setObjectName("month_label")
        self.day_label = QtWidgets.QLabel(self.centralwidget)
        self.day_label.setGeometry(QtCore.QRect(100, 210, 221, 16))
        self.day_label.setObjectName("day_label")
        self.hour_label = QtWidgets.QLabel(self.centralwidget)
        self.hour_label.setGeometry(QtCore.QRect(100, 260, 221, 16))
        self.hour_label.setObjectName("hour_label")
        self.button_of_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_of_save.setGeometry(QtCore.QRect(450, 350, 75, 23))
        self.button_of_save.setObjectName("button_of_save")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(100, 80, 221, 20))
        self.name.setObjectName("name")
        self.year = QtWidgets.QLineEdit(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(100, 130, 71, 20))
        self.year.setObjectName("year")
        self.month = QtWidgets.QLineEdit(self.centralwidget)
        self.month.setGeometry(QtCore.QRect(100, 180, 71, 20))
        self.month.setObjectName("month")
        self.day = QtWidgets.QLineEdit(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(100, 230, 71, 20))
        self.day.setObjectName("day")
        self.hour = QtWidgets.QLineEdit(self.centralwidget)
        self.hour.setGeometry(QtCore.QRect(100, 280, 71, 20))
        self.hour.setObjectName("hour")
        self.minutes = QtWidgets.QLineEdit(self.centralwidget)
        self.minutes.setGeometry(QtCore.QRect(100, 330, 71, 20))
        self.minutes.setObjectName("minutes")
        self.minutes_label = QtWidgets.QLabel(self.centralwidget)
        self.minutes_label.setGeometry(QtCore.QRect(100, 310, 221, 16))
        self.minutes_label.setObjectName("minutes_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.name_label.setText(_translate("MainWindow", "название"))
        self.year_label.setText(_translate("MainWindow", "год"))
        self.month_label.setText(_translate("MainWindow", "месяц"))
        self.day_label.setText(_translate("MainWindow", "день"))
        self.hour_label.setText(_translate("MainWindow", "час"))
        self.button_of_save.setText(_translate("MainWindow", "сохранить"))
        self.minutes_label.setText(_translate("MainWindow", "минуты"))
