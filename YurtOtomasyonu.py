import sqlite3
from KullaniciGirisi import YetkiliKaydiOlustur, OgrenciKaydiOlustur, YetkiliGiris, OgrenciGiris
from veritabaniQT5 import Ui_MainWindow
from PencereIslemleri import *
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import GrafikIslemleri
from girisekrani import *



baglanti = sqlite3.connect("Yurt.db")
isaretci = baglanti.cursor()


class Ogrenci():

    def __init__(self, ):
        pass

    def YemekleriGoster(self):

        isaretci.execute("SELECT * FROM Yemekler ORDER BY Yemek_Tarih")
        veriler = isaretci.fetchall()

        for i in veriler:
            print(i)

    def DuyurulariGoster(self):

        isaretci.execute("SELECT * FROM Duyurular ORDER BY Duyuru_Tarih")
        veriler = isaretci.fetchall()

        for i in veriler:
            print(i)

    def ArayuzOgrenci(self):

        print("""
                    
                    İşlemler
                    
                    1-Bilgilerim
                    2-Karta para yükle
                    3-Yemekleri göster
                    4-Duyuruları göster
                    5-Uygulamayı kapat 
                   
        """)

class Yurt():

    def __init__(self, ad="-", soyad="-", yas=0, tcNo=0, okul="-", bolum="-", telefonNo=0,
                 Durum="Aktif", OdenecekTutar=0, KalanTutar = 0, sozlesme=0, sehir="", kayittarih=0, odasecimi=0,
                 yurtIsmi="", yatakSayisi = 0, TekKisilikFiyat = 0, CiftKisilikFiyat = 0, UcKisilikFiyat = 0):
        self.durum = Durum
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.okul = okul
        self.bolum = bolum
        self.telefonno = telefonNo
        self.tutar = OdenecekTutar
        self.tcno = tcNo
        self.kalantutar = KalanTutar
        self.sozlesme = sozlesme
        self.sehir = sehir
        self.kayittarih = kayittarih
        self.odasecimi = odasecimi
        self.yurtismi = yurtIsmi
        self.yatakSayisi = yatakSayisi
        self.tek_fiyat = TekKisilikFiyat
        self.cift_fiyat = CiftKisilikFiyat
        self.uc_fiyat = UcKisilikFiyat

    def OgrenciEkle(self):  # Öğrenci ekle
        try:
            sayi = int(input("Sisteme kaç tane öğrenci ekleyeceksiniz:"))
            sayac = 1
            for i in range(0, sayi):

                ad = input("{}. Öğrenci için Ad:".format(sayac, self.ad))
                soyad = input("{}. Öğrenci için Soyad:".format(sayac, self.soyad))
                yas = int(input("{}. Öğrenci için Yaş:".format(sayac, self.yas)))
                tcNo = input("{}. Öğrenci için Tc No:".format(sayac, self.tcno))
                while len(tcNo) != 11:
                    tcNo = input("Tc No 11 haneli olmalıdır!\nTekrar deneyiniz:")

                okul = input("{}. Öğrenci için Okul:".format(sayac, self.okul))
                bolum = input("{}. Öğrenci için Bölüm:".format(sayac, self.bolum))
                telefon = input("{}. Ögrenci için Telefon Numarası(Örn:537..):".format(sayac, self.telefonno))

                """isaretci.execute("SELECT OdaSlotu1, OdaSlotu2, OdaSlotu3 FROM bilgileryurt")
                veriler = isaretci.fetchone()

                for i in veriler:
                    print(i)"""

                nakit = input("Toplam tutar nakit mi ödenecek?(E/H):")

                if nakit == 'E' or nakit == 'e':
                    self.KalanTutar = 0

                elif nakit == 'H' or nakit == 'h':

                    OdenecekTutar = int(input("{}. Öğrenci için ödenecek aylık tutar(TL):".format(sayac, self.tutar)))
                    sozlesme = int(input("{}.Öğrenci için Sözleşme kaç kay olacak?".format(sayac, self.sozlesme)))

                    self.KalanTutar = (OdenecekTutar*sozlesme / sozlesme)

                sehir = input("{}. Öğrenci için Şehir:".format(sayac, self.sehir))

                simdi = datetime.datetime.now()
                kayittarih = simdi.strftime("%d/%m/%Y")

                print("Başarılı!")

                sayac += 1

                isaretci.execute(
                    "create table if not exists bilgilerogrenci"
                    "(ad TEXT NOT NULL,"
                    "soyad TEXT NOT NULL,"
                    "yas INT NOT NULL,"
                    "TCNO INT NOT NULL, "
                    "okul TEXT,"
                    "bolum TEXT, "
                    "telefon INT, "
                    "KalanTutar INT NOT NULL, "
                    "sehir TEXT, "
                    "kayittarih TEXT)"
                )
                baglanti.commit()
                isaretci.execute(
                    "insert into bilgilerogrenci values('{}','{}',{}, {} ,'{}','{}', {}, {}, '{}', '{}')"
                        .format(ad, soyad, yas, tcNo, okul, bolum, telefon, self.KalanTutar, sehir, kayittarih))
                baglanti.commit()
                Pencere_Basarili()

        except ValueError:
            print("Yanlış değer girdiniz, Tekrar deneyiniz!")
            Pencere_Basarisiz()
        except ZeroDivisionError:
            print("0'a Bölünme hatası meydana geldi!")
            Pencere_Basarisiz()

    def OgrenciSil(self):  # Öğrenci sil

        try:
            NeyeGore = int(input("Neye göre öğrenci silmek istersiniz?\n1-Ad ve soyad\n2-Tc No\n3-ID"))

            if NeyeGore == 1:
                ad = input("Silinecek öğrencinin adını giriniz:")
                soyad = input("Silinecek öğrencinin soyadını giriniz:")
                isaretci.execute("Delete From bilgilerogrenci where ad LIKE '%'||?||'%' AND soyad LIKE '%'||?||'%'", (ad, soyad,))
                baglanti.commit()
                print("Öğrenci başarıyla silindi")

                Pencere_Basarili()

            elif NeyeGore == 2:
                tcNo = input("Silinecek öğrencinin TC Kimlik Numarasını giriniz:")

                while len(tcNo) != 11:
                    tcNo = input("TC Kimlik Numarası 11 haneli olmalıdır!\nSilinecek öğrencinin TC Kimlik Numarasını giriniz:")

                isaretci.execute("Delete From bilgilerogrenci where TCNO = ?", (tcNo,))
                baglanti.commit()
                print("Öğrenci başarıyla silindi")

                Pencere_Basarili()

            elif NeyeGore == 3:
                isaretci.execute("select * from bilgilerogrenci")  # Verileri oku
                veriler = isaretci.fetchall()  # Tüm verileri al
                sayac = 0

                for i in veriler:
                    print("{}. Öğrencinin bilgileri:{}:".format(sayac + 1, i))
                    sayac += 1

                ID = int(input("Silmek istediğiniz öğrencinin ID'sini giriniz:"))

                isaretci.execute("DELETE FROM bilgilerogrenci WHERE ROWID = ?", (ID,))
                baglanti.commit()
                print("Öğrenci başarıyla silindi")

                Pencere_Basarili()



        except ValueError or IndexError:
            print("Geçerli değer giriniz!")
            Pencere_Basarisiz()

    def OgrenciAra(self):
        NeyeGore = int(input("Neye göre arama yapmak istersiniz?\n1-Ad soyad\n2-Tc No"))

        if NeyeGore == 1:

            try:
                ad = input("Aranacak öğrencinin adını giriniz:")
                soyad = input("Aranacak öğrencinin soyadını giriniz:")

                # Kullanıcı tam ad veya soyad girmese bile arama optimizasyonu sayesinde öğrenci bulunabilir
                sonuclar = isaretci.execute("SELECT * FROM bilgilerogrenci WHERE ad LIKE '%'||?||'%' AND soyad LIKE '%'||?||'%'", (ad, soyad,))
                baglanti.commit()

                if sonuclar:
                    for i in sonuclar:
                        print("{} Adlı öğrencinin bilgileri:{}".format(i[0], i))

                elif sonuclar == False:
                    print("Öğrenci bulunamadı!")

            except ValueError:
                print("Ad veya soyad kısmına yanlış değer girdiniz!")

        elif NeyeGore == 2:

            try:
                tcno = int(input("Aranacak öğrencinin Tc Kimlik Numarasını giriniz:"))

                sonuclar = isaretci.execute("SELECT * FROM bilgilerogrenci WHERE TCNO = ?", (tcno,))
                baglanti.commit()

                if sonuclar:
                    for i in sonuclar:
                        print("{} Tc Kimlik Numaralı öğrencinin bilgileri:{}".format(i[3], i))
            except ValueError:
                print("TC Kimlik numarası kısmına yanlış değer girdiniz!")

    def OgrenciFiltrele(self):
        filtrele = int(input("Öğrencileri neye göre filtrelemek istiyorsunuz?\n1-Ad Soyad\n2-Tc Kimlik Numarası\n3-Yaş"
                           "\n4-Telefon Numarası\n5-Şehir"))

        if filtrele == 1:
            sonuclar=isaretci.execute("SELECT ad, soyad FROM bilgilerogrenci ORDER BY ad")

            for i in sonuclar:
                    print("Öğrencinin Adı ve Soyadı:{}".format(i), end="\n")

        elif filtrele == 2:
            sonuclar = isaretci.execute("SELECT ad, TCNO FROM bilgilerogrenci ORDER BY TCNO")

            for i in sonuclar:
                    print("Öğrencinin adı ve Kimlik Numarası : {} ".format(i))

        elif filtrele == 3:
            sonuclar = isaretci.execute("SELECT ad, yas FROM bilgilerogrenci ORDER BY yas ASC")
            for i in sonuclar:
                    print("Öğrencinin adı ve yaşı:{} ".format(i))

            ortalama = isaretci.execute("SELECT AVG(yas) FROM bilgilerogrenci")
            for i in ortalama:
                print("\nÖğrencilerin yaş ortalaması:{}".format(i))

        elif filtrele == 4:

            sonuclar = isaretci.execute("SELECT ad, telefon FROM bilgilerogrenci ORDER BY ad, telefon")
            for i in sonuclar:
                print("Öğrencinin adı ve Telefon Numarası: {}".format(i))

        elif filtrele == 5:
            sonuclar = isaretci.execute("SELECT sehir FROM bilgilerogrenci ORDER BY sehir")

            for i in sonuclar:
                print("")

    def OgrenciBilgileri(self):

        isaretci.execute("select * from bilgilerogrenci")  # Verileri oku
        veriler = isaretci.fetchall()  # Tüm verileri al
        sayac = 0

        for i in veriler:
                print("{}. Öğrencinin bilgileri:{}:".format(sayac + 1, i))
                sayac += 1

        isaretci.execute("select *from bilgilerogrenci")  # Verileri oku
        ogrsayisi = len(isaretci.fetchall())  # Satır sayısını al
        print("Sistemde toplam {} öğrenci var.".format(ogrsayisi))

        ### Veri tabanını ekranda göstermek için yapılan işlem ###

        if __name__ == "__main__":
            import sys

            uygulama = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ekran = Ui_MainWindow()
            ekran.setupUi(MainWindow)
            MainWindow.show()
            print("Veri tabanı açıldı!")
            uygulama.exec_()

    def OgrenciBilgiGuncelle(self):

        isaretci.execute("select * from bilgilerogrenci")
        veriler = isaretci.fetchall()
        sayac = 0

        for i in veriler:
            print("{}. Öğrencinin bilgileri: {}".format(sayac+1, i), sep="-")
            sayac += 1

        secim = int(input("Kaçıncı öğrencinin bilgilerini güncellemek istiyorsunuz?\nSeçiniz:"))

        ad = input("{}. Öğrenci için Ad:".format(secim, self.ad))
        soyad = input("{}. Öğrenci için Soyad:".format(secim, self.soyad))
        yas = int(input("{}. Öğrenci için Yaş:".format(secim, self.yas)))
        tcNo = input("{}. Öğrenci için Tc No:".format(secim, self.tcno))
        while len(tcNo) != 11:
            tcNo = input("Tc No 11 haneli olmalıdır!\nTekrar deneyiniz:")

        okul = input("{}. Öğrenci için Okul:".format(secim, self.okul))
        bolum = input("{}. Öğrenci için Bölüm:".format(secim, self.bolum))
        telefon = input("{}. Ögrenci için Telefon Numarası(Örn:537..):".format(secim, self.telefonno))

        nakit = input("Toplam tutar nakit mi ödenecek?(E/H):")

        if nakit == 'E' or nakit == 'e':
            self.KalanTutar = 0

        elif nakit == 'H' or nakit == 'h':

            OdenecekTutar = int(input("{}. Öğrenci için ödenecek aylık tutar(TL):".format(secim, self.tutar)))
            sozlesme = int(input("{}.Öğrenci için Sözleşme kaç kay olacak?".format(secim, self.sozlesme)))

            self.KalanTutar = (OdenecekTutar * sozlesme / sozlesme)

        sehir = input("{}. Öğrenci için Şehir:".format(sayac, self.sehir))

        simdi = datetime.datetime.now()
        kayittarih = simdi.strftime("%d/%m/%Y")

        isaretci.execute("UPDATE bilgilerogrenci SET ad = '{}', soyad = '{}', yas = {}, TCNO = {}, okul = '{}', "
                         "bolum = '{}', telefon = {}, KalanTutar = {}, sehir = '{}', kayittarih = '{}'  WHERE ROWID = {}"
                         .format(ad, soyad, yas, tcNo, okul, bolum, telefon, self.KalanTutar, sehir, kayittarih, secim))

        baglanti.commit() #Güncellemeyi gerçekleştirmek için commit ettik

    def SaatTarih(self):

       simdi = datetime.datetime.now()

       saat_tarih = simdi.strftime("%d/%m/%Y, %H:%M:%S")
       print("Tarih ve Saat:{}".format(saat_tarih))

    def Kapat(self):
        quit()

    def YurtBilgisiGiris(self):
        isaretci.execute("create table if not exists bilgileryurt"
                            "(yurtIsmi TEXT, yatakSayisi INT, Tek_Fiyat INT, Cift_Fiyat INT, Uc_Fiyat INT)")

        self.yurtismi = input("Yurt ismini giriniz:")
        self.yataksayisi = int(input("Yatak sayısını giriniz:"))
        self.tek_fiyat = int(input("Tek kişilik odanızın fiyatını giriniz:"))
        self.cift_fiyat = int(input("Çift kişilik odanızın fiyatını giriniz:"))
        self.uc_fiyat = int(input("Üç kişilik odanızın fiyatını giriniz:"))

        if self.tek_fiyat == 0 or self.cift_fiyat == 0 or self.uc_fiyat == 0:
            self.tek_fiyat, self.cift_fiyat, self.uc_fiyat = 1, 1, 1

        ############################################################################

        isaretci.execute(
            "INSERT INTO bilgileryurt values('{}', {}, {}, {}, {})"
                .format(self.yurtismi, self.yataksayisi, self.tek_fiyat, self.cift_fiyat, self.uc_fiyat))

        baglanti.commit()


    def YurtBilgisiGoster(self):
        isaretci.execute("select * from bilgileryurt")
        sonuclar = isaretci.fetchone()

        for i in sonuclar:
            print("Yurt ismi:{}".format(i))
            break

        isaretci.execute("select * from bilgilerogrenci")  # Verileri oku
        ogrsayisi = len(isaretci.fetchall())  # Satır sayısını al
        print("Sistemde toplam {} öğrenci var.".format(ogrsayisi))

        isaretci.execute("select * from bilgilerogrenci")  # Verileri oku
        print("Sistemde toplam {} yatak var.".format(self.yatakSayisi - ogrsayisi))



    def Istatistikler(self):
        secim = int(input("1-Öğrencilerin yaş grafiğini göster\n"
                      "2-Öğrencilerin geldiği şehirlerin grafiğini göster\n"
                      "3-Toplam kazanç / zarar grafiğini göster\nSeçim yapınız:"))
        if secim == 1:
            GrafikIslemleri.Grafik_Yas()

        elif secim == 2:
            pass

        elif secim == 3:
            GrafikIslemleri.Grafik_KarZarar()

    def YemekBilgisiGiris(self):

        isaretci.execute("CREATE TABLE IF NOT EXISTS Yemekler(Yemek_Tarih TEXT, Yemek_Bir TEXT, Yemek_İki TEXT, "
                         "Yemek_Uc TEXT, Yemek_Ek TEXT)")

        Kac_Kere = int(input("Kaç tane yemek girişi yapacaksınız:"))

        for i in range(1, Kac_Kere+1):

            yemek_Tarih = input("{}. Yemek tarihini giriniz:".format(i))
            yemek_Corba = input("{} için Çorba:".format(yemek_Tarih))
            yemek_Ana =  input("{} için Ana yemek:".format(yemek_Tarih))
            yemek_Ana2 = input("{} için Ana yemek 2:".format(yemek_Tarih))
            yemek_Ek = input("{} için Tatlı/Salata/İçecek:".format(yemek_Tarih))

            isaretci.execute("INSERT INTO Yemekler values('{}' ,'{}', '{}', '{}', '{}')".format(yemek_Tarih, yemek_Corba,
                                                                                              yemek_Ana, yemek_Ana2,
                                                                                              yemek_Ek))
        baglanti.commit()


    def DuyuruIslemleri(self):

        secim = int(input("1-Duyuru Ekle\n"
                      "2-Duyuru Sil\nSeçiniz:"))

        if secim == 1:

            isaretci.execute("CREATE TABLE IF NOT EXISTS Duyurular(Duyuru_Tarih TEXT, Duyuru TEXT)")
            duyuru_Tarih = datetime.datetime.now()
            duyuru = input("Duyuruyu giriniz:")

            isaretci.execute("INSERT INTO Duyurular values('{}', '{}')".format(duyuru_Tarih, duyuru))

            baglanti.commit()

        elif secim == 2:

            isaretci.execute("SELECT * FROM Duyurular")
            veriler = isaretci.fetchall()
            sayac = 0

            for i in veriler:
                print("{}. Duyuru: {}".format(sayac+1, i))

            kacinci = int(input("Kaçıncı duyuruyu silmek istiyorsunuz:"))

            isaretci.execute("DELETE FROM Duyurular WHERE ROWID = {} ".format(kacinci))

    def ArayuzYurt(self):

        print("""
                            İşlemler
                            
                            1-Öğrenci ekle 
                            2-Öğrenci sil 
                            3-Öğrenci ara 
                            4-Öğrenci bilgileri 
                            5-Öğrenci filtrele 
                            6-Öğrenci bilgisi güncelle
                            7-Yemek bilgisi girişi
                            8-Yurt bilgileri 
                            9-Yurt istatistikleri 
                            10-Duyuru işlemleri
                            11-Uygulamayı kapat                       
                """)

ogrenci1 = Ogrenci()
yurt1 = Yurt()


secimGiris = int(input("1-Yeni Kullanıcı Oluştur\n2-Öğrenci girişi yap\n3-Yetkili girişi yap\nSeçiniz:"))

if secimGiris == 1:

    secim = int(input("1-Yetkili kaydı yap\n2-Öğrenci kaydı yap\nSeçiniz:"))

    if secim == 1:
        YetkiliKaydiOlustur()
        yurt1.YurtBilgisiGiris()
        yurt1.ArayuzYurt()

    elif secim == 2:
        OgrenciKaydiOlustur()
        ogrenci1.ArayuzOgrenci()


elif secimGiris == 2:

    if OgrenciGiris():

        while True:

            yurt1.SaatTarih()
            ogrenci1.ArayuzOgrenci()
            secim1 = int(input("Yapmak istediğiniz işlemi seçiniz:"))

            if secim1 == 3:
                ogrenci1.YemekleriGoster()

            elif secim1 == 4:
	            ogrenci1.DuyurulariGoster()

elif secimGiris == 3:

    if YetkiliGiris():

        while True:

            yurt1.ArayuzYurt()
            yurt1.SaatTarih()

            secim1 = int(input("Yapmak istediğiniz işlemi seçiniz:"))

            if secim1 == 1:
                yurt1.OgrenciEkle()

            elif secim1 == 2:
                yurt1.OgrenciBilgileri()
                yurt1.OgrenciSil()

            elif secim1 == 3:
                yurt1.OgrenciAra()

            elif secim1 == 4:
                yurt1.OgrenciBilgileri()


            elif secim1 == 5:
                yurt1.OgrenciFiltrele()

            elif secim1 == 6:
                yurt1.OgrenciBilgiGuncelle()

            elif secim1 == 7:
                yurt1.YemekBilgisiGiris()

            elif secim1 == 8:
                    yurt1.YurtBilgisiGoster()

            elif secim1 == 9:
                yurt1.Istatistikler()

            elif secim1 == 10:
                yurt1.DuyuruIslemleri()

            elif secim1 == 11:
                exit()

