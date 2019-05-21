import sqlite3
from KullaniciGirisi import kullanicilar1
from veritabaniQT5 import Ui_MainWindow
from PencereIslemleri import *
import datetime
from PyQt5 import QtWidgets
import GrafikIslemleri
import os

baglanti = sqlite3.connect("Yurt.db")
isaretci = baglanti.cursor()

#  bilgilerogrenci adlı tabloyu oluşturduk

isaretci.execute(
                    "create table if not exists bilgilerogrenci"
                    "(ad TEXT NOT NULL,"
                    "soyad TEXT NOT NULL,"
                    "yas INT NOT NULL,"
                    "cinsiyet TEXT NOT NULL,"
                    "TCNO INT NOT NULL,"
                    "okul TEXT,"
                    "bolum TEXT, "
                    "telefon INT, "
                    "KalanTutar INT NOT NULL, "
                    "sehir TEXT, "
                    "kayittarih TEXT)"
                )


def EkranTemizle():
    os.system('cls')


class Ogrenci():

    def __init__(self, ):
        pass


    def YemekleriGoster(self):

        EkranTemizle()
        isaretci.execute("SELECT * FROM Yemekler ORDER BY Yemek_Tarih")
        veriler = isaretci.fetchall()

        for i in veriler:
            print(i)

    def DuyurulariGoster(self):

        EkranTemizle()
        isaretci.execute("SELECT * FROM Duyurular ORDER BY Duyuru_Tarih")
        veriler = isaretci.fetchall()

        for i in veriler:
            print(i)

    def OgrenciBilgileriGuncelle(self):

        EkranTemizle()
        kullanicilar1.OgrenciBilgilerimiGuncelle()

    def ArayuzOgrenci(self):

        print("""
                    
                    İşlemler
                    
                    1-BİLGİLERİM
                    2-YEMEKLERİ GÖSTER
                    3-DUYURULARI GÖSTER
                    4-BİLGİLERİMİ GÜNCELLE
                    5-ÇIKIŞ
                   
        """)

class Yurt():

    def __init__(self, ad="-", soyad="-", yas=0, tcNo=0, okul="-", bolum="-", telefonNo=0,
                 OdenecekTutar=0, KalanTutar = 0, sozlesme=0, sehir="", kayittarih=0, odasecimi=0,
                 yurtIsmi="-", yatakSayisi = 0, Cinsiyet="-"):
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
        self.cinsiyet = Cinsiyet


    def OgrenciEkle(self):  # Öğrenci ekle
        EkranTemizle()
        try:
            sayi = int(input("Sisteme kaç tane öğrenci ekleyeceksiniz:"))
            sayac = 1
            for i in range(0, sayi):

                self.ad = input("{}. Öğrenci için Ad:".format(sayac))
                self.soyad = input("{}. Öğrenci için Soyad:".format(sayac))
                self.yas = int(input("{}. Öğrenci için Yaş:".format(sayac)))
                self.cinsiyet = input("{}. Öğrenci için Cinsiyet(K/E):".format(sayac))
                self.tcNo = input("{}. Öğrenci için Tc No:".format(sayac))
                while len(self.tcNo) != 11:
                    Pencere_Basarisiz()
                    self.tcNo = input("Tc No 11 haneli olmalıdır!\nTekrar deneyiniz:")

                self.okul = input("{}. Öğrenci için Okul:".format(sayac))
                self.bolum = input("{}. Öğrenci için Bölüm:".format(sayac))
                self.telefonno = input("{}. Ögrenci için Telefon Numarası(Örn:537..):".format(sayac))

                nakit = input("Toplam tutar nakit mi ödenecek?(E/H):")

                if nakit == 'E' or nakit == 'e':
                    self.KalanTutar = 0

                elif nakit == 'H' or nakit == 'h':

                    self.tutar = int(input("{}. Öğrenci için ödenecek aylık tutar(TL):".format(sayac)))
                    self.sozlesme = int(input("{}. Öğrenci için Sözleşme kaç kay olacak:".format(sayac)))

                    self.KalanTutar = (self.tutar*self.sozlesme / self.sozlesme)

                self.sehir = input("{}. Öğrenci için Şehir:".format(sayac))

                simdi = datetime.datetime.now()
                kayittarih = simdi.strftime("%d/%m/%Y")

                sayac += 1

                baglanti.commit()
                isaretci.execute(
                    "insert into bilgilerogrenci values('{}','{}',{}, '{}' ,{} ,'{}','{}', {}, {}, '{}', '{}')"
                        .format(self.ad, self.soyad, self.yas, self.cinsiyet, self.tcNo, self.okul, self.bolum,
                                self.telefonno, self.KalanTutar, self.sehir, kayittarih))
                baglanti.commit()
                Pencere_Basarili()

        except ValueError:
            print("Yanlış değer girdiniz, Tekrar deneyiniz!")
            Pencere_Basarisiz()
        except ZeroDivisionError:
            print("0'a Bölünme hatası meydana geldi!")
            Pencere_Basarisiz()

    def OgrenciSil(self):  # Öğrenci sil
        EkranTemizle()
        try:
            NeyeGore = int(input("Neye göre öğrenci silmek istersiniz?\n1-Ad ve soyad\n2-Tc No\n3-ID\nSeçiniz:"))

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
        EkranTemizle()
        NeyeGore = int(input("Neye göre arama yapmak istersiniz?\n1-Ad soyad\n2-Tc No\nSeçiniz:"))

        if NeyeGore == 1:

            try:
                ad = input("Aranacak öğrencinin adını giriniz:")
                soyad = input("Aranacak öğrencinin soyadını giriniz:")

                # Kullanıcı tam ad veya soyad girmese bile arama optimizasyonu sayesinde öğrenci bulunabilir
                sonuclar = isaretci.execute("SELECT * FROM bilgilerogrenci WHERE ad LIKE '%'||?||'%' AND soyad "
                                            "LIKE '%'||?||'%'", (ad, soyad,))
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

                sonuclar = isaretci.execute("SELECT * FROM bilgilerogrenci WHERE TCNO = ?", (tcno,))  # Tc no al
                baglanti.commit()

                if sonuclar:
                    for i in sonuclar:
                        print("{} Tc Kimlik Numaralı öğrencinin bilgileri:{}".format(i[3], i))
            except ValueError:
                print("TC Kimlik numarası kısmına yanlış değer girdiniz!")

    def OgrenciFiltrele(self):
        EkranTemizle()
        filtrele = int(input("Öğrencileri neye göre filtrelemek istiyorsunuz?\n1-Ad Soyad\n2-Tc Kimlik Numarası\n3-Yaş\n"
                             "4-Telefon Numarası\n5-Şehir\nSeçiniz:"))

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
            sonuclar = isaretci.execute("SELECT ad, sehir FROM bilgilerogrenci ORDER BY sehir")

            for i in sonuclar:
                print("Öğrencinin adı ve geldiği şehir: {}".format(i))

    def OgrenciBilgileri(self):
        EkranTemizle()
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

        EkranTemizle()
        isaretci.execute("select * from bilgilerogrenci")
        veriler = isaretci.fetchall()
        sayac = 0

        for i in veriler:
            print("{}. Öğrencinin bilgileri: {}".format(sayac+1, i))
            sayac += 1

        secim = int(input("Kaçıncı öğrencinin bilgilerini güncellemek istiyorsunuz?\nSeçiniz:"))

        self.ad = input("{}. Öğrenci için Ad:".format(secim))
        self.soyad = input("{}. Öğrenci için Soyad:".format(secim))
        self.yas = int(input("{}. Öğrenci için Yaş:".format(secim)))
        self.cinsiyet = input("{}. Öğrenci için Cinsiyet(K/E):".format(secim))
        self.tcNo = input("{}. Öğrenci için Tc No:".format(secim))
        while len(self.tcNo) != 11:
            Pencere_Basarisiz()
            self.tcNo = input("Tc No 11 haneli olmalıdır!\nTekrar deneyiniz:")

        self.okul = input("{}. Öğrenci için Okul:".format(secim))
        self.bolum = input("{}. Öğrenci için Bölüm:".format(secim))
        self.telefonno = input("{}. Ögrenci için Telefon Numarası(Örn:537..):".format(secim))

        nakit = input("Toplam tutar nakit mi ödenecek?(E/H):")

        if nakit == 'E' or nakit == 'e':
            self.KalanTutar = 0

        elif nakit == 'H' or nakit == 'h':

            self.tutar = int(input("{}. Öğrenci için ödenecek aylık tutar(TL):".format(secim)))
            self.sozlesme = int(input("{}. Öğrenci için Sözleşme kaç kay olacak:".format(secim)))

            self.KalanTutar = (self.tutar * self.sozlesme / self.sozlesme)

        self.sehir = input("{}. Öğrenci için Şehir:".format(secim))

        simdi = datetime.datetime.now()
        kayittarih = simdi.strftime("%d/%m/%Y")

        sayac += 1

        isaretci.execute("UPDATE bilgilerogrenci SET ad = ?, soyad = ?, yas = ?, cinsiyet = ?, TCNO = ?, "
                         "okul = ?, bolum = ?, telefon = ?, KalanTutar = ?, sehir = ?, "
                         "kayittarih = ?  WHERE ROWID = ?", (self.ad, self.soyad, self.yas, self.cinsiyet, self.tcNo,
                                                             self.okul, self.bolum,
                                                             self.telefonno, self.KalanTutar, self.sehir, kayittarih,
                                                             secim,))
        Pencere_Basarili()
        baglanti.commit()  # Güncellemeyi gerçekleştirmek için

    def SaatTarih(self):

        simdi = datetime.datetime.now()

        saat_tarih = simdi.strftime("%d/%m/%Y, %H:%M:%S")
        print("Tarih ve Saat:{}".format(saat_tarih))

    def Kapat(self):
        quit()

    def YurtBilgisiGoster(self):

        EkranTemizle()
        isaretci.execute("SELECT * FROM bilgileryurt")
        sonuclar = isaretci.fetchall()

        for i in sonuclar:
            print("Yurt ismi:{}".format(i[1]))
            break

        isaretci.execute("select * from bilgilerogrenci")  # Verileri oku
        ogrsayisi = len(isaretci.fetchall())  # Satır sayısını al
        print("Sistemde toplam {} öğrenci var.".format(ogrsayisi))

        isaretci.execute("select * from bilgilerogrenci")  # Verileri oku
        print("Sistemde toplam {} yatak var.".format(self.yatakSayisi - ogrsayisi))

    def Grafikler(self):
        EkranTemizle()
        secim_grafik = int(input("1-Öğrencilerin yaş grafiğini göster\n"
                                 "2-Öğrencilerin geldiği şehirlerin grafiğini göster\n"
                                 "3-Toplam kazanç / zarar grafiğini göster\n4-Cinsiyet grafiğini göster"
                                 "\nSeçim yapınız:"))
        if secim_grafik == 1:
            GrafikIslemleri.Grafik_Yas()

        elif secim_grafik == 2:
            GrafikIslemleri.Grafik_Sehir()

        elif secim_grafik == 3:
            GrafikIslemleri.Grafik_KarZarar()

        elif secim_grafik == 4:
            GrafikIslemleri.Grafik_Cinsiyet()

    def YemekBilgisiGiris(self):

        EkranTemizle()
        isaretci.execute("CREATE TABLE IF NOT EXISTS Yemekler(Yemek_Tarih TEXT, Yemek_Bir TEXT, Yemek_İki TEXT, "
                         "Yemek_Uc TEXT, Yemek_Ek TEXT)")

        Kac_Kere = int(input("Kaç tane yemek girişi yapacaksınız:"))

        for i in range(1, Kac_Kere+1):

            yemek_Tarih = input("{}. Yemek tarihini giriniz:".format(i))
            yemek_Corba = input("{} için Çorba:".format(yemek_Tarih))
            yemek_Ana =  input("{} için Yemek 1:".format(yemek_Tarih))
            yemek_Ana2 = input("{} için Yemek 2:".format(yemek_Tarih))
            yemek_Ek = input("{} için Tatlı/Salata/İçecek:".format(yemek_Tarih))

            isaretci.execute("INSERT INTO Yemekler values('{}' ,'{}', '{}', '{}', '{}')".format(yemek_Tarih, yemek_Corba
                                                                                                , yemek_Ana, yemek_Ana2
                                                                                                , yemek_Ek))
        baglanti.commit()

    def DuyuruIslemleri(self):

        EkranTemizle()
        secim = int(input("1-Duyuru Ekle\n2-Duyuru Sil\nSeçiniz:"))

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

    def HarcamaGirisi(self):
        EkranTemizle()
        isaretci.execute("CREATE TABLE IF NOT EXISTS YurtGiderleri(Harcama_Aciklama TEXT, Harcama_Miktar INT)")

        kacAdet = int(input("Kaç tane harcama girişi yapacaksınız:"))

        for sayac in range(1, kacAdet+1):

            harcama_aciklama = input("{}. Harcama açıklaması:".format(sayac))
            harcama_miktar = int(input("{}. Harcama miktarı:".format(sayac)))

            isaretci.execute("INSERT INTO YurtGiderleri values('{}', {})".format(harcama_aciklama, harcama_miktar))

    def YetkiliBilgileriGuncelle(self):

        EkranTemizle()

        kullanicilar1.YetkiliBilgilerimiGuncelle()

    def ArayuzYurt(self):

        print("""
                            İşlemler
                            
                            
                            1-ÖĞRENCİ İŞLEMLERİ
                            2-YURT İŞLEMLERİ
                            3-BİLGİLERİM
                            4-BİLGİLERİMİ GÜNCELLE
                            5-ÇIKIŞ                      
                """)


ogrenci1 = Ogrenci()
yurt1 = Yurt()

secimGiris = int(input("1-Yeni Kullanıcı Oluştur\n2-Öğrenci girişi yap\n3-Yetkili girişi yap\nSeçiniz:"))

if secimGiris == 1:

    secim = int(input("1-Yetkili kaydı yap\n2-Öğrenci kaydı yap\nSeçiniz:"))

    if secim == 1:
        kullanicilar1.YetkiliKaydiOlustur()
        yurt1.ArayuzYurt()

    elif secim == 2:
        kullanicilar1.OgrenciKaydiOlustur()
        ogrenci1.ArayuzOgrenci()


elif secimGiris == 2:

    if kullanicilar1.OgrenciGiris():

        while True:


            yurt1.SaatTarih()
            ogrenci1.ArayuzOgrenci()
            secim1 = int(input("Yapmak istediğiniz işlemi seçiniz:"))

            if secim1 == 1:
                kullanicilar1.OgrenciBilgilerim()

            elif secim1 == 2:
                ogrenci1.YemekleriGoster()

            elif secim1 == 3:
                ogrenci1.DuyurulariGoster()

            elif secim1 == 4:
                ogrenci1.OgrenciBilgileriGuncelle()

            elif secim1 == 5:
                exit()

elif secimGiris == 3:

    if kullanicilar1.YetkiliGiris():

        while True:

            yurt1.ArayuzYurt()
            yurt1.SaatTarih()

            secim1 = int(input("Yapmak istediğiniz işlemi seçiniz:"))

            if secim1 == 1:

                ogrenci_islemi = int(input("1-Öğrenci Ekle\n2-Öğrenci sil\n3-Öğrenci ara\n4-Öğrenci bilgileri\n"
                                           "5-Öğrenci filtrele\n6-Öğrenci bilgisi güncelle\nSeçiniz:"))

                if ogrenci_islemi == 1:
                    yurt1.OgrenciEkle()

                elif ogrenci_islemi == 2:
                    yurt1.OgrenciBilgileri()
                    yurt1.OgrenciSil()

                elif ogrenci_islemi == 3:
                    yurt1.OgrenciAra()

                elif ogrenci_islemi == 4:
                    yurt1.OgrenciBilgileri()

                elif ogrenci_islemi == 5:
                    yurt1.OgrenciFiltrele()

                elif ogrenci_islemi == 6:
                    yurt1.OgrenciBilgiGuncelle()

            elif secim1 == 2:

                yurt_islemi = int(input("1-Yemek bilgisi girişi\n2-Yurt bilgisi göster\n3-Yurt istatistikleri\n"
                                        "4-Duyuru işlemleri\n5-Harcama girişi\nSeçiniz:"))

                if yurt_islemi == 1:
                    yurt1.YemekBilgisiGiris()

                elif yurt_islemi == 2:
                    yurt1.YurtBilgisiGoster()

                elif yurt_islemi == 3:
                    yurt1.Grafikler()

                elif yurt_islemi == 4:
                    yurt1.DuyuruIslemleri()

                elif yurt_islemi == 5:
                    yurt1.HarcamaGirisi()

            elif secim1 == 3:
                kullanicilar1.YetkiliBilgilerim()

            elif secim1 == 4:
                yurt1.YetkiliBilgileriGuncelle()

            elif secim1 == 5:
                exit()
