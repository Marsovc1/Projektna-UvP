from Matrika_GUI import *
from program_vezni import *
from Orodje import *
import tkinter as tk

def zaganjalec_matrik():
    st = int(st_vnos.get())
    okno3.destroy()
    for i in range(st):
        matrika()

okno3 = tk.Tk()

st_mat = tk.Label(okno3, text='Koliko matrik bos uporabil? ')
st_mat.grid(row=0, column=0)
st_vnos = tk.Entry(okno3)
st_vnos.grid(row=0, column=1)

nadaljuj_gumb = tk.Button(okno3, text='Nadaljuj', command=zaganjalec_matrik)
nadaljuj_gumb.grid(row=1, columnspan=2)

okno3.mainloop()