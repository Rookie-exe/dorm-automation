import matplotlib.pyplot as plt
import sqlite3
from PencereIslemleri import *

baglanti = sqlite3.connect("Yurt.db")
isaretci = baglanti.cursor()

# Yaş grafiği

def Grafik_Yas():
	isaretci.execute("SELECT DISTINCT yas FROM bilgilerogrenci")
	yaslar=[]

	for i in isaretci.fetchall():
		yaslar.append(i)
		print(yaslar)

	araliklar = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

	plt.hist(yaslar, araliklar, histtype='bar')

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Yaş Grafiği')
	plt.legend()
	plt.show()

def Grafik_Ulke():
	pass

def Grafik_KarZarar():

		isaretci.execute("select SUM(KalanTutar) from bilgilerogrenci")
		toplam_kazanc = isaretci.fetchall()

		print("Aylık toplam kazancınız:{}".format(toplam_kazanc))

		isaretci.execute("select SUM(toplam_harcama) from yurtgiderleri")
		toplam_harcama = isaretci.fetchall()
		print("Aylık toplam harcamanız:{}".format(toplam_harcama))

		araliklar = [0, 1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000]

		plt.hist(toplam_kazanc, araliklar, histtype='bar')

		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Kar Zarar grafiği')
		plt.legend()
		plt.show()







