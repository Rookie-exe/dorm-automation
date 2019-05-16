# Aşağıdaki kodların bir kısmını QT Designer programı kullanarak basit bir arayüz tasarladım ve buraya aktardım

from PyQt5 import QtCore, QtGui, QtWidgets


import sqlite3

class Ui_MainWindow(object):

    def Veritabani_Goster(self):
        baglanti = sqlite3.connect("Yurt.db")
        sorgu = "SELECT * FROM bilgilerogrenci"
        self.tableWidget.setRowCount(5)

        sonuc = baglanti.execute(sorgu)

        for satir_sayisi, satir_verisi in enumerate(sonuc):
            self.tableWidget.insertRow(satir_sayisi)
            for sutun_sayisi, veri in enumerate(satir_verisi):
                self.tableWidget.setItem(satir_sayisi, sutun_sayisi, QtWidgets.QTableWidgetItem(str(veri)))
        baglanti.close()


    def ButtonAyari(self):
        self.btn_goster.setEnabled(False)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 781, 401))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_goster = QtWidgets.QPushButton(self.centralwidget)
        self.btn_goster.setGeometry(QtCore.QRect(320, 460, 121, 31))
        self.btn_goster.setObjectName("btn_goster")

        self.btn_goster.clicked.connect(self.Veritabani_Goster)
        self.btn_goster.clicked.connect(self.ButtonAyari)

        basliklar = ["AD", "SOYAD", "YAŞ", "TC_NO", "OKUL", "BÖLÜM", "TEL_NO", "AYLIK_ODENEN", "ŞEHİR", "KAYIT_TARİHİ"]
        self.tableWidget.setHorizontalHeaderLabels(basliklar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ogrenciler", "Öğrenciler"))
        self.btn_goster.setText(_translate("MainWindow", "Verileri  Göster"))



