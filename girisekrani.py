# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girisekrani.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PencereIslemleri import *


class Ui_GirisEkrani(object):

    def __init__(self):
        pass

    def giris(self):

        kullanici_adi = self.lineEdit.text()
        sifre = self.lineEdit_2.text()

        baglanti = sqlite3.connect("Yurt.db")
        sonuc = baglanti.execute("SELECT * FROM kullanicilar2 WHERE kullaniciadi = ? AND sifre = ?", (kullanici_adi, sifre))
        baglanti.commit()

        if(len(sonuc.fetchall()) > 0 ):
            print("Giriş yapıldı!")
            Pencere_Basarili()
            QtWidgets.qApp.closeAllWindows()

        else:
            print("Kullanıcı bulunamadı!\nTekrar deneyiniz")
            Pencere_Basarisiz()
            return False



    def setupUi(self, GirisEkrani):
        GirisEkrani.setObjectName("GirisEkrani")
        GirisEkrani.resize(865, 600)
        font = QtGui.QFont()
        font.setItalic(False)
        GirisEkrani.setFont(font)
        GirisEkrani.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        GirisEkrani.setMouseTracking(False)
        GirisEkrani.setAutoFillBackground(False)
        GirisEkrani.setStyleSheet("background-color: rgb(89, 170, 132);")
        GirisEkrani.setTabShape(QtWidgets.QTabWidget.Rounded)
        GirisEkrani.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(GirisEkrani)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(430, 160, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(85, 85, 0);\n"
"background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Kullanıcı adınız...")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 170, 0);\n"
"background-color: rgb(170, 85, 0);\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 300, 111, 61))
        self.pushButton.clicked.connect(self.giris)
        font = QtGui.QFont()
        font.setFamily("Nyala")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(650, 540, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(247, 390, 371, 181))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.dateTimeEdit.raise_()
        self.calendarWidget.raise_()
        GirisEkrani.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GirisEkrani)
        self.statusbar.setObjectName("statusbar")
        GirisEkrani.setStatusBar(self.statusbar)

        self.retranslateUi(GirisEkrani)
        QtCore.QMetaObject.connectSlotsByName(GirisEkrani)

    def retranslateUi(self, GirisEkrani):
        _translate = QtCore.QCoreApplication.translate
        GirisEkrani.setWindowTitle(_translate("GirisEkrani", "Giriş Ekranı"))
        self.label.setText(_translate("GirisEkrani", "Kullanıcı adı:"))
        self.label_2.setText(_translate("GirisEkrani", "Şifre:"))
        self.lineEdit.setWhatsThis(_translate("GirisEkrani", "<html><head/><body><p>Kullanıcı adı girişi</p></body></html>"))
        self.lineEdit_2.setWhatsThis(_translate("GirisEkrani", "<html><head/><body><p>Şifre girişi</p></body></html>"))
        self.pushButton.setText(_translate("GirisEkrani", "Giriş yap"))


"""def Calistir():
    if __name__ == "__main__":
        import sys

        uygulama = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ekran = Ui_GirisEkrani()
        ekran.setupUi(MainWindow)
        MainWindow.show()
        print("Giriş ekranı Açıldı")
        uygulama.exec_()

        if girisekrani.giris():
            QtWidgets.qApp.closeAllWindows()




girisekrani = Ui_GirisEkrani()"""













