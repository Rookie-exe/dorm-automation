import sqlite3

baglanti = sqlite3.connect("Yurt.db")
isaretci = baglanti.cursor()
isaretci.execute("create table if not exists yetkililer(ad TEXT,soyad TEXT,kullaniciadi TEXT, sifre TEXT)") # Yetkili Tablosu olusturma
isaretci.execute("create table if not exists ogrenciler(ad TEXT,soyad TEXT,kullaniciadi TEXT, sifre TEXT)") # Öğrenci Tablosu olusturma

baglanti.commit()

def KullaniciOlustur():

    global kullaniciadi
    KullaniciSecim = int(input("1-Yetkili kullanıcı oluştur\n2-Öğrenci kullanıcı oluştur\nSeçiniz:"))

    if KullaniciSecim == 1:
        bulundu = 0
        dogrulama = int(input("Size özel verilen BeniOku.txt dosyasındaki doğrulama kodunu giriniz:"))

        if dogrulama == 35494848:

            while bulundu == 0:

                kullaniciadi = input("Bir kullanıcı adı oluşturunuz:")

                k_bul = ("SELECT * FROM yetkililer WHERE kullaniciadi=?")
                isaretci.execute(k_bul, [(kullaniciadi)])

                if isaretci.fetchall():  # True değer dönerse böyle bir kadi oldugunu bulmus olucaz
                    print("Kullanıcı adı kullanılıyor!\nTekrar deneyiniz")

                else:
                    bulundu = 1

            ad = input("Adınızı giriniz:")
            soyad = input("Soyadınızı giriniz:")  #### Bilgileri kullanicidan aldik ####

            sifre = input("Bir şifre oluşturunuz:")
            sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

            while sifre != sifre1:
                print("Yanlış girdiniz!\nOluşturduğunuz şifreyi tekrar giriniz:")
                sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

            isaretci.execute("INSERT INTO yetkililer values('{}','{}','{}','{}') ".format(ad, soyad, kullaniciadi, sifre))  # Tabloya verileri girme
            baglanti.commit()
            print("Kullanıcı başarıyla oluşturuldu!")

            girisYap = str(input("Sisteme giriş yapmak ister misiniz?(E/H):"))
            if girisYap == 'E' or girisYap == 'e':
                YetkiliGiris()
            else:
                exit()
        else:
            print("Yanlış girdiniz!\nÇıkış yapılıyor...")
            exit()

    elif KullaniciSecim == 2:

        bulundu = 0

        while bulundu == 0:

            kullaniciadi = input("Bir kullanıcı adı oluşturunuz:")

            k_bul = ("SELECT * FROM ogrenciler WHERE kullaniciadi=?")
            isaretci.execute(k_bul, [(kullaniciadi)])

            if isaretci.fetchall():  #True değer dönerse böyle bir kadi oldugunu bulmus olucaz
                print("Kullanıcı adı kullanılıyor!\nTekrar deneyiniz")

            else:
                bulundu = 1

        ad = input("Adınızı giriniz:")
        soyad = input("Soyadınızı giriniz:")  #### Bilgileri kullanicidan aldik ####

        sifre = input("Bir şifre oluşturunuz:")
        sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

        while sifre != sifre1:
            print("Yanlış girdiniz!\nOluşturduğunuz şifreyi tekrar giriniz:")
            sifre1 = input("Oluşturduğunuz şifreyi tekrar giriniz:")

        isaretci.execute("INSERT INTO ogrenciler values('{}','{}','{}','{}') ".format(ad, soyad, kullaniciadi, sifre))  # Tabloya verileri girme
        baglanti.commit()
        print("Kullanıcı başarıyla oluşturuldu!")

        girisYap = str(input("Sisteme giriş yapmak ister misiniz?(E/H):"))
        if girisYap == 'E' or girisYap == 'e':
            OgrenciGiris()
        else:
            exit()

def YetkiliGiris():

        while True:
            kullaniciadi = input("Kullanıcı adınızı giriniz:")
            sifre = input("Şifrenizi giriniz:")

            # ************************************************************************* #

                        #####   Kullanıcının verilerini doğrulama işlemi #####

            k_bul = ("SELECT * FROM yetkililer WHERE kullaniciadi = ? AND sifre = ?")
            isaretci.execute(k_bul, [(kullaniciadi), (sifre)])
            sonuclar = isaretci.fetchall()

            # ************************************************************************* #
            baglanti.commit()

            if sonuclar:
                for i in sonuclar:
                    print("Hoş geldin "+i[0])  #0. indekste ad oldugu icin
                return True
            else:

                print("Kullanıcı adı ve/veya şifre yanlış!")

                secim = input("Tekrar denemek ister misiniz? (E/H):")

                if secim == 'E' or secim == 'e':
                    YetkiliGiris()
                else:
                    break



def OgrenciGiris():

    while True:
        kullaniciadi = input("Kullanıcı adınızı giriniz:")
        sifre = input("Şifrenizi giriniz:")

        # ************************************************************************* #

        #####   Kullanıcının verilerini doğrulama işlemi #####

        k_bul = ("SELECT * FROM ogrenciler WHERE kullaniciadi = ? AND sifre = ?")
        isaretci.execute(k_bul, [(kullaniciadi), (sifre)])
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
                OgrenciGiris()
            else:
                break








