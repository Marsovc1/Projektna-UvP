import tkinter as tk


def je_naravno_stevilo(a):
    try:
        stevilo = float(a)
        if stevilo > 0:
            if int(stevilo) == stevilo:
                return True
    except ValueError:
        return False

def error_okno():
    okno_error = tk.Tk()
    error = tk.Label(okno_error, text='Vnesi naravno število')
    error.grid(row=0, column=0)
    gumbOK = tk.Button(okno_error, text='OK', command=okno_error.destroy)
    gumbOK.grid(row=1, column=0)

