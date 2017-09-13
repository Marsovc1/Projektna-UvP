from Matrika_GUI import *
from program_vezni import *
from Orodje import *
import tkinter as tk
import ast

def operacija():
    okno4 = tk.Tk()

    st_mat = tk.Label(okno4, text='Vnesi ime matrike v okenca')
    st_mat.grid(row=0, columnspan=2)

    matrika1 = tk.Entry(okno4)
    matrika1.grid(row=1, column=0)
    matrika2 = tk.Entry(okno4)
    matrika2.grid(row=1, column=1)

    def preberi():
        global mat1
        global mat2
        prva = matrika1.get()
        druga = matrika2.get()
        mat1 = ast.literal_eval(open(str(prva)+'.txt', 'r').read())
        mat2 = ast.literal_eval(open(str(druga)+'.txt', 'r').read())
        print(mat1, mat2)

    gumb_beri = tk.Button(okno4, text='Preberi matriki', command=preberi)
    gumb_beri.grid(row=2, column=0)
    gumbsest = tk.Button(okno4, text='Seštej 1. in 2. matriko', command=lambda: seštevalec_matrik(mat1, mat2))
    gumbsest.grid(row=2, column=1)
    gumbodst = tk.Button(okno4, text='Odštej 2. matriko od 1.', command=lambda: odštevalec_matrik(mat1, mat2))
    gumbodst.grid(row=3, column=0)
    gumbodst2 = tk.Button(okno4, text='Odštej 1. matriko od 2.', command=lambda: odštevalec_matrik(mat2, mat1))
    gumbodst2.grid(row=3, column=1)
    okno4.mainloop()

def zaganjalec_matrik():
    st = st_vnos.get()
    if je_naravno_stevilo(st):
        okno3.destroy()
        for i in range(int(st)):
            matrika()
        operacija()
    else:
        error_okno()

okno3 = tk.Tk()

st_mat = tk.Label(okno3, text='Koliko matrik bos uporabil? ')
st_mat.grid(row=0, column=0)
st_vnos = tk.Entry(okno3)
st_vnos.grid(row=0, column=1)

nadaljuj_gumb = tk.Button(okno3, text='Nadaljuj', command=zaganjalec_matrik)
nadaljuj_gumb.grid(row=1, columnspan=2)

okno3.mainloop()