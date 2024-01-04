from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = Tk()
root.title("Aplikasi Diabetes")
style = ttk.Style("darkly")

def hitung_risiko():
    gula_darah = float(entry1.get())
    tekanan_darah = float(entry2.get())
    
    if gula_darah < 70:
        hasil = "Level gula darah rendah. Segera konsultasikan dengan dokter."
    elif 70 <= gula_darah <= 120:
        hasil ="Level gula darah normal Dan Tidak Mengalami Diabetes"
    elif 120 <= gula_darah <= 200:
        hasil = "Level gula darah tinggi. Segera konsultasikan dengan dokter Dan Akan Mengalami Resiko Diabetes"
    else:
        hasil = "Anda Terkena Diabetes."

    hasil1["text"] = hasil

gula_darah = Label(root, text="Kadar Gula Darah:")
gula_darah.grid(column=0, row=0, padx=10, pady=10)
entry1 = Entry(root)
entry1.grid(column=1, row=0, padx=10, pady=10)

tekanan_darah = Label(root, text="Tekanan Darah:")
tekanan_darah.grid(column=0, row=1, padx=10, pady=10)
entry2 = Entry(root)
entry2.grid(column=1, row=1, padx=10, pady=10)

btn = Button(root, text="Hitung Risiko", command=hitung_risiko)
btn.grid(column=0, row=2, columnspan=2, pady=10)

hasil1 = Label(root, text="")
hasil1.grid(column=0, row=3, columnspan=2, pady=10)

root.mainloop()
