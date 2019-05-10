from tkinter import *


def Pencere_Basarili():
    pencere = Tk()
    pencere.resizable(width=FALSE, height=FALSE)
    baslik = pencere.title("Uyarı")
    etiket = Label(pencere, text="Başarılı!")
    buton1 = Button(pencere, text="Tamam", command=pencere.destroy)

    etiket.pack()
    buton1.pack()

    pencere_yukseklik = 150
    pencere_genislik = 300

    ekran_genislik = pencere.winfo_screenwidth()
    ekran_yukseklik = pencere.winfo_screenheight()

    x = int((ekran_genislik / 2) - (pencere_genislik / 2))
    y = int((ekran_yukseklik / 2) - (pencere_yukseklik / 2))

    pencere.geometry("{}x{}+{}+{}".format(pencere_genislik, pencere_yukseklik, x, y))
    mainloop()

def Pencere_Basarisiz():
	pencere = Tk()
	pencere.resizable(width=FALSE, height=FALSE)
	baslik = pencere.title("Uyarı")
	etiket = Label(pencere, text="Başarısız!")
	buton1 = Button(pencere, text="Tamam", command=pencere.destroy)

	etiket.pack()
	buton1.pack()

	pencere_yukseklik = 150
	pencere_genislik = 300

	ekran_genislik = pencere.winfo_screenwidth()
	ekran_yukseklik = pencere.winfo_screenheight()

	x = int((ekran_genislik / 2) - (pencere_genislik / 2))
	y = int((ekran_yukseklik / 2) - (pencere_yukseklik / 2))

	pencere.geometry("{}x{}+{}+{}".format(pencere_genislik, pencere_yukseklik, x, y))
	mainloop()
