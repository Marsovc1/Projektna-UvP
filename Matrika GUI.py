import tkinter as tk

def matrika():
    okno = tk.Tk()

    vrsticeA = tk.Label(okno, text='število vrstic matrike A')
    vrsticeA.grid(row=0, column=0)
    vhodvrst = tk.Entry(okno)
    vhodvrst.grid(row=0, column=1)

    stolpciA = tk.Label(okno, text='število stolpcev matrike A')
    stolpciA.grid(row=1, column=0)
    vhodstolp = tk.Entry(okno)
    vhodstolp.grid(row=1, column=1)

    vrsticeB = tk.Label(okno, text='število vrstic matrike B')
    vrsticeB.grid(row=2, column=0)
    vhodvrstB = tk.Entry(okno)
    vhodvrstB.grid(row=2, column=1)

    stolpciB = tk.Label(okno, text='število stolpcev matrike B')
    stolpciB.grid(row=3, column=0)
    vhodstolpB = tk.Entry(okno)
    vhodstolpB.grid(row=3, column=1)

    def preveri_vrednosti():
        try:
            a1 = int(vhodvrst.get())
            a2 = int(vhodstolp.get())
            b2 = int(vhodstolpB.get())
            b1 = int(vhodvrstB.get())

            vrednost = {}
            matrika = tk.Tk()
            for vrsta in range(a1):
                for stolpec in range(a2):
                    indeks = (vrsta, stolpec)
                    vhodelement = tk.Entry(matrika)
                    vhodelement.grid(row=vrsta+1, column=stolpec)
                    vrednost[indeks] = vhodelement

            def podatki_matrike():
                matrikaA = []
                for vrsta in range(a1):
                    vrstica = []
                    for stolpec in range(a2):
                        indeks = (vrsta, stolpec)
                        vrstica.append(vrednost[indeks].get())
                    matrikaA.append(vrstica)
                return matrikaA

            gumb = tk.Button(matrika, text='Začni', command=podatki_matrike)
            gumb.grid(row=a1+1, columnspan=2)

        except ValueError:
            print('Vnesi naravni števili')

    gumb = tk.Button(okno, text='Začni', command=preveri_vrednosti)
    gumb.grid(row=4, columnspan=2)

    okno.mainloop()