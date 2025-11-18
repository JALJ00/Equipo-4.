# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazgWduqt.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1376, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cmdSalir = QPushButton(self.centralwidget)
        self.cmdSalir.setObjectName(u"cmdSalir")
        self.cmdSalir.setGeometry(QRect(120, 520, 75, 31))
        font = QFont()
        font.setBold(True)
        self.cmdSalir.setFont(font)
        self.cmdConectar = QPushButton(self.centralwidget)
        self.cmdConectar.setObjectName(u"cmdConectar")
        self.cmdConectar.setGeometry(QRect(20, 520, 75, 31))
        self.cmdConectar.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 300, 131, 61))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(210, 290, 560, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTemp1 = QLCDNumber(self.horizontalLayoutWidget)
        self.lblTemp1.setObjectName(u"lblTemp1")

        self.horizontalLayout.addWidget(self.lblTemp1)

        self.lblTemp2 = QLCDNumber(self.horizontalLayoutWidget)
        self.lblTemp2.setObjectName(u"lblTemp2")

        self.horizontalLayout.addWidget(self.lblTemp2)

        self.lblTemp3 = QLCDNumber(self.horizontalLayoutWidget)
        self.lblTemp3.setObjectName(u"lblTemp3")

        self.horizontalLayout.addWidget(self.lblTemp3)

        self.lblTemp4 = QLCDNumber(self.horizontalLayoutWidget)
        self.lblTemp4.setObjectName(u"lblTemp4")

        self.horizontalLayout.addWidget(self.lblTemp4)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(220, 20, 541, 261))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pbTemp1 = QProgressBar(self.horizontalLayoutWidget_2)
        self.pbTemp1.setObjectName(u"pbTemp1")
        self.pbTemp1.setMinimumSize(QSize(0, 0))
        self.pbTemp1.setValue(10)
        self.pbTemp1.setOrientation(Qt.Orientation.Vertical)
        self.pbTemp1.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.pbTemp1)

        self.pbTemp2 = QProgressBar(self.horizontalLayoutWidget_2)
        self.pbTemp2.setObjectName(u"pbTemp2")
        self.pbTemp2.setValue(0)
        self.pbTemp2.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.pbTemp2)

        self.pbTemp3 = QProgressBar(self.horizontalLayoutWidget_2)
        self.pbTemp3.setObjectName(u"pbTemp3")
        self.pbTemp3.setValue(0)
        self.pbTemp3.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.pbTemp3)

        self.pbTemp4 = QProgressBar(self.horizontalLayoutWidget_2)
        self.pbTemp4.setObjectName(u"pbTemp4")
        self.pbTemp4.setSizeIncrement(QSize(10, 0))
        self.pbTemp4.setValue(0)
        self.pbTemp4.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.pbTemp4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(790, 300, 131, 61))
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(980, 20, 160, 261))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pbHum1 = QProgressBar(self.horizontalLayoutWidget_3)
        self.pbHum1.setObjectName(u"pbHum1")
        self.pbHum1.setValue(24)
        self.pbHum1.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_3.addWidget(self.pbHum1)

        self.pbHum2 = QProgressBar(self.horizontalLayoutWidget_3)
        self.pbHum2.setObjectName(u"pbHum2")
        self.pbHum2.setValue(24)
        self.pbHum2.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_3.addWidget(self.pbHum2)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(920, 290, 278, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lblHum1 = QLCDNumber(self.horizontalLayoutWidget_4)
        self.lblHum1.setObjectName(u"lblHum1")

        self.horizontalLayout_4.addWidget(self.lblHum1)

        self.lblHum2 = QLCDNumber(self.horizontalLayoutWidget_4)
        self.lblHum2.setObjectName(u"lblHum2")

        self.horizontalLayout_4.addWidget(self.lblHum2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 380, 71, 41))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 380, 71, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 380, 81, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(670, 380, 71, 41))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(960, 380, 71, 41))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1100, 380, 71, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1376, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cmdSalir.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.cmdConectar.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Temperatura: </span></p></body></html>", None))
        self.pbTemp1.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Humedad:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">DHT1:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">DHT2:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">lm35-1:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">lm35-2</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">DHT1:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">DHT1:</span></p></body></html>", None))
    # retranslateUi

