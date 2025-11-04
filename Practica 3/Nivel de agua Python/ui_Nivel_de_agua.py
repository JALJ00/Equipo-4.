# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nivel de aguaeKcgSO.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ProBar = QProgressBar(self.centralwidget)
        self.ProBar.setObjectName(u"ProBar")
        self.ProBar.setGeometry(QRect(180, 240, 351, 121))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.ProBar.setFont(font)
        self.ProBar.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ProBar.setMaximum(20)
        self.ProBar.setValue(0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 0, 301, 101))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 280, 121, 41))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 280, 131, 31))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 261, 51))
        font3 = QFont()
        font3.setPointSize(28)
        font3.setItalic(True)
        self.label_4.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 953, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nivel de Agua", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nivel min", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nivel Max", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cantidad en (L)", None))
    # retranslateUi

