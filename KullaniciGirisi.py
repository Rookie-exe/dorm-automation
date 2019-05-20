import sqlite3
from PencereIslemleri import Pencere_Basarisiz, Pencere_Basarili
baglanti = sqlite3.connect("Yurt.db")
isaretci = baglanti.cursor()

# Yetkili Tablosu olusturma
isaretci.execute("create table if not exists yetkililer(ad TEXT,soyad TEXT,kullaniciadi TEXT, sifre TEXT)")
# Öğrenci Tablosu olusturma
isaretci.execute("create table if not exists ogrenciler(ad TEXT,soyad TEXT,kullaniciadi TEXT, sifre TEXT)")

baglanti.commit()

class Kullanicilar():

    def __init__(self):
        pass

    def YetkiliKaydiOlustur(self):
        global yetkili_kullaniciadi
        bulundu = 0
        dogrulama = int(input("Size özel verilen BeniOku.txt dosyasındaki doğrulama kodunu giriniz:"))

        if dogrulama == 35494848:

            while bulundu == 0:

                yetkili_kullaniciadi = input("Bir kullanıcı adı oluşturunuz:")

                k_bul = ("SELECT * FROM yetkililer WHERE kullaniciadi=?")
                isaretci.execute(k_bul, [(yetkili_kullaniciadi)])

                if isaretci.fetchall():  # True değer dönerse böyle bir kadi oldugunu bulmus olucaz
                    print("Kullanıcı adı kullanılıyor!\nTekrar deneyiniz")

                else:
                    bulundu = 1

            ad = input("Adınızı giriniz:")
            soyad = input("Soyadınızı giriniz:")
            #### Bilgileri kullanicidan aldik ####
            sifre = input("Bir şifre oluşturunuz:")
            sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")



            while sifre != sifre1:
                Pencere_Basarisiz()
                print("Yanlış girdiniz!\nOluşturduğunuz şifreyi tekrar giriniz:")
                sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

            isaretci.execute("create table if not exists bilgileryurt"
                             "(yurtSahibi TEXT, yurtIsmi TEXT, yatakSayisi INT")

            yurtismi = input("Yurt ismini giriniz:")
            yataksayisi = int(input("Yatak sayısını giriniz:"))                    # Yurt bilgilerini aldık

            # Tabloya verileri girme
            isaretci.execute("INSERT INTO yetkililer values('{}','{}','{}','{}') ".format(ad, soyad,
                                                                                          yetkili_kullaniciadi, sifre))

            isaretci.execute("INSERT INTO bilgileryurt values('{}', '{}', {} )"
                             .format(yetkili_kullaniciadi, yurtismi, yataksayisi))

            baglanti.commit()
            print("Kullanıcı başarıyla oluşturuldu!")

            giris_yap = str(input("Sisteme giriş yapmak ister misiniz?(E/H):"))
            if giris_yap == 'E' or giris_yap == 'e':
                    Kullanicilar.YetkiliGiris(self)
            else:
                exit()
        else:
            print("Yanlış girdiniz!\nÇıkış yapılıyor...")
            Pencere_Basarisiz()
            exit()

    def OgrenciKaydiOlustur(self):

        global ogrenci_kullaniciadi
        bulundu = 0

        while bulundu == 0:

            ogrenci_kullaniciadi = input("Bir kullanıcı adı oluşturunuz:")

            k_bul = ("SELECT * FROM ogrenciler WHERE kullaniciadi = ?")
            isaretci.execute(k_bul, [(ogrenci_kullaniciadi)])

            if isaretci.fetchall():  # True değer dönerse böyle bir kadi oldugunu bulmus olucaz
                print("Kullanıcı adı kullanılıyor!\nTekrar deneyiniz")

            else:
                bulundu = 1

        ad = input("Adınızı giriniz:")
        soyad = input("Soyadınızı giriniz:")  #### Bilgileri kullanicidan aldik ####

        sifre = input("Bir şifre oluşturunuz:")
        sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

        while sifre != sifre1:
            Pencere_Basarisiz()
            print("Yanlış girdiniz!\nOluşturduğunuz şifreyi tekrar giriniz:")
            sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

        isaretci.execute("INSERT INTO ogrenciler values('{}','{}','{}','{}') ".format(ad, soyad, ogrenci_kullaniciadi,
                                                                                      sifre))  # Tabloya verileri girme

        baglanti.commit()
        print("Kullanıcı başarıyla oluşturuldu!")

        giris_yap = str(input("Sisteme giriş yapmak ister misiniz?(E/H):"))
        if giris_yap == 'E' or giris_yap == 'e':
            Kullanicilar.OgrenciGiris(self)
        else:
            exit()

    def YetkiliGiris(self):

            while True:
                global yetkili_kullaniciadi

                yetkili_kullaniciadi = input("Kullanıcı adınızı giriniz:")
                sifre = input("Şifrenizi giriniz:")

                # ************************************************************************* #

                            #####   Kullanıcının verilerini doğrulama işlemi #####

                k_bul = ("SELECT * FROM yetkililer WHERE kullaniciadi = ? AND sifre = ?")
                isaretci.execute(k_bul, [(yetkili_kullaniciadi), (sifre)])
                sonuclar = isaretci.fetchall()

                # ************************************************************************* #
                baglanti.commit()

                if sonuclar:


                    for i in sonuclar:
                        print("Hoş geldin "+i[0])  # 0. indekste ad olduğu için
                    return True
                else:

                    print("Kullanıcı adı ve/veya şifre yanlış!")

                    secim = input("Tekrar denemek ister misiniz? (E/H):")

                    if secim == 'E' or secim == 'e':
                        Kullanicilar.YetkiliGiris(self)
                    else:
                        break

    def OgrenciGiris(self):

        while True:
            global ogrenci_kullaniciadi
            ogrenci_kullaniciadi = input("Kullanıcı adınızı giriniz:")
            sifre = input("Şifrenizi giriniz:")

            # ************************************************************************* #

            #####   Kullanıcının verilerini doğrulama işlemi #####

            k_bul = ("SELECT * FROM ogrenciler WHERE kullaniciadi = ? AND sifre = ?")
            isaretci.execute(k_bul, [(ogrenci_kullaniciadi), (sifre)])
            sonuclar = isaretci.fetchall()

            # ************************************************************************* #
            baglanti.commit()

            if sonuclar:
                for i in sonuclar:
                    print("Hoş geldin " + i[0])

                return True
            else:

                print("Kullanıcı adı ve/veya şifre yanlış!")

                secim = input("Tekrar denemek ister misiniz? (E/H):")

                if secim == 'E' or secim == 'e':
                    Kullanicilar.OgrenciGiris(self)
                else:
                    break


    def OgrenciBilgilerim(self):

        global ogrenci_sonuclar
        #  Öğrencinin kullanıcı adını doğrulayıp tüm bilgilerini alma işlemi
        isaretci.execute('SELECT * FROM ogrenciler WHERE kullaniciadi = ? ', (ogrenci_kullaniciadi,))
        ogrenci_sonuclar = isaretci.fetchall()

        for j in ogrenci_sonuclar:
            print("Ad:{}".format(j[0]))
            print("Soyad:{}".format(j[1]))
            print("Kullanıcı adı: {}".format(j[2]))
            print("Şifre:{}".format(j[3]))

    def YetkiliBilgilerim(self):
        global yetkili_sonuclar
        #  Yetkilinin kullanıcı adını doğrulayıp tüm bilgilerini alma işlemi
        isaretci.execute('SELECT * FROM yetkililer WHERE kullaniciadi = ? ', (yetkili_kullaniciadi,))
        yetkili_sonuclar = isaretci.fetchall()

        for j in yetkili_sonuclar:
            print("Ad:{}".format(j[0]))     # Veri tabanından indekslere göre bilgileri aldık
            print("Soyad:{}".format(j[1]))
            print("Kullanıcı adı: {}".format(j[2]))
            print("Şifre:{}".format(j[3]))

    def OgrenciBilgilerimiGuncelle(self):

        bulundu = 0
        global ogrenci_kullaniciadi
        isaretci.execute('SELECT ROWID FROM ogrenciler WHERE kullaniciadi = ? ', (ogrenci_kullaniciadi,))
        ogrenci_no = isaretci.fetchall()

        while bulundu == 0:

            ogrenci_kullaniciadi = input("Yeni kullanıcı adınız:")

            k_bul = "SELECT * FROM ogrenciler WHERE kullaniciadi=?"
            isaretci.execute(k_bul, [ogrenci_kullaniciadi])

            if isaretci.fetchall():  # True değer dönerse böyle bir kadi oldugunu bulmus olucaz
                print("Kullanıcı adı kullanılıyor!\nTekrar deneyiniz")

            else:
                bulundu = 1

        ad = input("Yeni ad:")
        soyad = input("Yeni soyad:")  #### Bilgileri kullanicidan aldik ####

        sifre = input("Yeni şifre:")
        sifre1 = input("Yeni şifreyi tekrar giriniz:")

        while sifre != sifre1:
            Pencere_Basarisiz()
            print("Yanlış girdiniz!\nYeni şifreyi tekrar giriniz:")
            sifre1 = input("Yeni şifreyi tekrar giriniz:")

        isaretci.execute("UPDATE ogrenciler "
                         "SET kullaniciadi = ?, ad = ?, soyad = ?, sifre = ? "
                         "WHERE ROWID = ?", (ogrenci_kullaniciadi, ad, soyad, sifre, ogrenci_no,))  # Tabloya verileri girme

        baglanti.commit()

    def YetkiliBilgilerimiGuncelle(self):

        bulundu = 0
        global yetkili_kullaniciadi
        isaretci.execute('SELECT ROWID FROM yetkililer WHERE kullaniciadi = ? ', (yetkili_kullaniciadi,))
        yetkili_no = isaretci.fetchall()
        while bulundu == 0:

            yetkili_kullaniciadi = input("Yeni kullanıcı adı:")

            k_bul = "SELECT * FROM ogrenciler WHERE kullaniciadi=?"
            isaretci.execute(k_bul, [ogrenci_kullaniciadi])

            if isaretci.fetchall():  # True değer dönerse böyle bir kadi oldugunu bulmus olucaz
                print("Kullanıcı adı kullanılıyor!\nTekrar deneyiniz")
                Pencere_Basarisiz()

            else:
                bulundu = 1

        ad = input("Yeni ad:")
        soyad = input("Yeni soyad:")  #### Bilgileri kullanicidan aldik ####

        sifre = input("Yeni şifre:")
        sifre1 = input("Yeni şifreyi tekrar giriniz:")

        while sifre != sifre1:
            Pencere_Basarisiz()
            print("Yanlış girdiniz!\nYeni şifreyi tekrar giriniz:")
            sifre1 = input("Yeni şifreyi tekrar giriniz:")

        isaretci.execute("UPDATE yetkililer "
                         "SET kullaniciadi = ?, ad = ?, soyad = ?, sifre = ? "
                         "WHERE ROWID = ?", (ogrenci_kullaniciadi, ad, soyad, sifre, yetkili_no,)) # Verileri güncelleme

        baglanti.commit()


kullanicilar1 = Kullanicilar()





