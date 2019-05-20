from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

def Pencere_Basarili():
	messagebox.showinfo("Başarılı", "İşlem başarıyla gerçekleşti!")

def Pencere_Basarisiz():
	messagebox.showerror("Başarısız", "İşleminiz başarısız oldu!")