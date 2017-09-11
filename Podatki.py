import tkinter as tk

okno = tk.Tk()

vrsticeA = tk.Label(okno, text='vrst')
vrsticeA.grid(row=0, column=0)
vhodvrst = tk.Entry(okno)
vhodvrst.grid(row=0, column=1)

stolpciA = tk.Label(okno, text='stolp')
stolpciA.grid(row=1, column=0)
vhodstolp = tk.Entry(okno)
vhodstolp.grid(row=1, column=1)

def poberipodatke():
    try:
        a = int(vhodvrst.get())
        b = int(vhodstolp.get())
        vrednost = {}

        matrika = tk.Tk()
        for vrsta in range(a):
            for stolpec in range(b):
                indeks = (vrsta, stolpec)
                vhodelement = tk.Entry(matrika)
                vhodelement.grid(row=vrsta, column=stolpec)
                vrednost[indeks] = vhodelement

        def podatki_matrike():
            matrika = []
            for vrsta in range(a):
                vrstica = []
                for stolpec in range(b):
                    indeks = (vrsta, stolpec)
                    vrstica.append(vrednost[indeks].get())
                matrika.append(vrstica)
            print(matrika)

        gumb = tk.Button(matrika, text='Začni', command=podatki_matrike)
        gumb.grid(row=a + 1, columnspan=3)

    except ValueError:
        print('Vnesi naravni števili')

gumb = tk.Button(okno, text='Začni', command=poberipodatke)
gumb.grid(row=2, columnspan=2)

okno.mainloop()