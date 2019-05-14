# Todo
#Yetkili kullanıcı girişi(kaydı) ve Öğrenci girişi(kaydı) adlı iki fonksiyon oluştur
#Eğer yetkili girişi yapılacaksa özel kod istensin


from tkinter import *
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('Yurt.db') as db:
    isaretci = db.cursor()

isaretci.execute("create table if not exists yetkililer(ad TEXT,soyad TEXT,kullaniciadi TEXT, sifre TEXT)") # Yetkili Tablosu olusturma
isaretci.execute("create table if not exists ogrenciler(ad TEXT,soyad TEXT,kullaniciadi TEXT, sifre TEXT)") # Öğrenci Tablosu olusturma
db.commit()
db.close()


# Kullanıcılar sınıfı

class Kullanicilar:
    def __init__(self, master):

        self.master = master

        self.ad = StringVar()
        self.soyad = StringVar()
        self.kullaniciadi = StringVar()
        self.sifre = StringVar()
        self.yeni_kullaniciadi = StringVar()
        self.yeni_sifre = StringVar()

        self.Arayuz()

    # Giriş fonksiyonu
    def GirisYap(self):

        with sqlite3.connect('Yurt.db') as db:
            isaretci = db.cursor()

        # Kullanıcı bulma işlemi
        find_user = ('SELECT * FROM yetkililer WHERE kullaniciadi = ? and sifre = ?')
        isaretci.execute(find_user ,[(self.kullaniciadi.get()), (self.sifre.get())])
        result = isaretci.fetchall()
        if result:
            self.logf.pack_forget()

            self.head['text'] = 'Hoşgeldiniz  ' + self.kullaniciadi.get()
            self.head['pady'] = 150
        else:
            ms.showerror('Hata', 'Kullanıcı adı bulunamadı')

    def YetkiliKaydiOlustur(self):

        with sqlite3.connect('Yurt.db') as db:
            isaretci = db.cursor()

        # Kullanıcı adı kontrol etme işlemi
        k_bul = ('SELECT * FROM yetkililer WHERE kullaniciadi = ?')
        isaretci.execute(k_bul, [(self.yeni_kullaniciadi.get())])
        if isaretci.fetchall():
            ms.showerror('Hata!', 'Kullanıcı adı kullanılıyor')
        else:
            ms.showinfo('Başarılı', 'Kullanıcı oluşturuldu.')
            self.GirisEkrani()
            insert = 'INSERT INTO yetkililer(ad, soyad, kullaniciadi, sifre) VALUES(?,?,?,?)'
            isaretci.execute(insert, [(self.ad.get()), (self.soyad.get()), (self.yeni_kullaniciadi.get()),
                                      (self.yeni_sifre.get())])
        db.commit()

    def GirisEkrani(self):
        self.kullaniciadi.set('')
        self.sifre.set('')
        self.kayit.pack_forget()
        self.head['text'] = 'Giriş'
        self.logf.pack()
    def KayitEkrani(self):
        self.ad.set('')
        self.soyad.set('')
        self.yeni_kullaniciadi.set('')
        self.yeni_sifre.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Kayıt'
        self.kayit.pack()

    # Arayüz fonksiyonu
    def Arayuz(self):
        self.head = Label(self.master ,text = 'Giriş' ,font = ('', 35), pady = 10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)


        Label(self.logf ,text = 'Kullanıcı adı: ' ,font = ('' ,20) ,pady=5 ,padx=5).grid(sticky = W)
        Entry(self.logf ,textvariable = self.kullaniciadi ,bd = 5 ,font = ('' ,15)).grid(row=0 ,column=1)
        Label(self.logf ,text = 'Şifre: ' ,font = ('' ,20) ,pady=5 ,padx=5).grid(sticky = W)
        Entry(self.logf ,textvariable = self.sifre ,bd = 5 ,font = ('' ,15) ,show = '*').grid(row=1 ,column=1)
        Button(self.logf ,text = ' Giriş yap ' ,bd = 3 ,font=('', 15), padx=5, pady=5, command=self.GirisYap).grid()
        Button(self.logf, text=' Kayıt yap ', bd=3, font=('', 15), padx=5, pady=5, command=self.KayitEkrani).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.kayit = Frame(self.master, padx=10, pady=10)

        Label(self.kayit, text='Ad: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.kayit, textvariable=self.ad, bd=5, font=('', 15)).grid(row=0, column=1)

        Label(self.kayit, text='Soyad: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.kayit, textvariable=self.soyad, bd=5, font=('', 15)).grid(row=1, column=1)
        Label(self.kayit, text='Kullanıcı adı: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.kayit, textvariable=self.yeni_kullaniciadi, bd=5, font=('', 15)).grid(row=2, column=1)
        Label(self.kayit, text='Şifre: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.kayit, textvariable=self.yeni_sifre, bd=5, font=('', 15), show='*').grid(row=3, column=1)

        Button(self.kayit, text='Kayıt yap', bd=3, font=('', 15), padx=5, pady=5, command=self.YetkiliKaydiOlustur).grid()
        Button(self.kayit, text='Giriş yap', bd=3, font=('', 15), padx=5, pady=5, command=self.GirisEkrani).grid(row=4,
                                                                                                         column=1)




root = Tk()
Kullanicilar(root)
root.mainloop()


