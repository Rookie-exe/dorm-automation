import matplotlib.pyplot as plt
import sqlite3

baglanti = sqlite3.connect("Yurt.db")
isaretci = baglanti.cursor()

# Yaş grafiği

def Grafik_Yas():
	isaretci.execute("SELECT yas FROM bilgilerogrenci")
	yaslar=[]

	for i in isaretci.fetchall():
		yaslar.append(i)

	araliklar = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

	plt.hist(yaslar, araliklar, histtype='bar', align='left')

	plt.xlabel('Yaşlar')
	plt.title('Yaş Grafiği')
	plt.show()

def Grafik_Ulke():

	# Her şehri bir kere aldık
	isaretci.execute("SELECT DISTINCT sehir FROM bilgilerogrenci")
	sehirler = []

	veri_sehirler = isaretci.fetchall()

	for i in veri_sehirler:
		for j in i:  # Listeye dönüştürdük
			sehirler.append(j)

	# Her şehri sayıp gruplara ayırdık
	isaretci.execute("SELECT COUNT(sehir) FROM bilgilerogrenci GROUP BY sehir")

	veri_sayi = isaretci.fetchall()

	sehir_sayisi = []

	for i in veri_sayi:
		for j in i:         # Listeye dönüştürdük
			sehir_sayisi.append(j)

	print(sehir_sayisi)
	print(sehirler)

	plt.pie(sehir_sayisi, explode=None, labels=sehirler, shadow=True, autopct='%1.1f%%', startangle=90)
	plt.axis('equal')
	plt.show()

def Grafik_KarZarar():

		# Tüm öğrencilerin ödeyeceği toplam tutarı al
		isaretci.execute("select SUM(KalanTutar) from bilgilerogrenci")

		toplam_kazanc = isaretci.fetchall()

		print("Aylık toplam kazancınız:{}".format(toplam_kazanc))

		isaretci.execute("select SUM(Harcama_Miktar), from YurtGiderleri")
		isaretci.execute("SELECT Harcama_Aciklama FROM YurtGiderleri")

		toplam_harcama = isaretci.fetchall()

		print("Aylık toplam harcamanız:{}".format(toplam_harcama))

		araliklar = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

		plt.hist(toplam_kazanc, araliklar, histtype='bar', align='left', orientation='horizontal')
		plt.hist(toplam_harcama, araliklar, histtype='bar', align='left', orientation='horizontal')

		plt.xlabel('Aralıklar')
		plt.ylabel('y')
		plt.title('Kar Zarar grafiği')
		plt.show()

def Grafik_Cinsiyet():

	isaretci.execute("SELECT DISTINCT cinsiyet FROM bilgilerogrenci")
	cinsiyetler = []
	sayilar = []

	sonuclar = isaretci.fetchall()

	for i in sonuclar:
		for j in i:
			cinsiyetler.append(j)

	isaretci.execute("SELECT COUNT(cinsiyet) FROM bilgilerogrenci GROUP BY cinsiyet ")

	veriler_sayi = isaretci.fetchall()

	for i in veriler_sayi:
		for j in i:
			sayilar.append(j)

	plt.pie(sayilar, explode=None, labels=cinsiyetler, shadow=True, autopct='%1.1f%%', startangle=90)
	plt.axis('equal')

	plt.show()



