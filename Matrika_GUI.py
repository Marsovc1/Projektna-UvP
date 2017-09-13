from program_vezni import *


def matrika():
    okno2 = tk.Tk() #pozdravno Okno
    okno2.title('Pozdrav!')
    pozdrav = tk.Label(okno2, text='To je orodje za operacije matrik :)')
    pozdrav.grid(row=0, columnspan=2)
    # navodila = tk.Label(okno2, text='Za vsako matri')
    # navodila.grid(row=1, columnspan=2)

    #poskus poljubnega imena: problem... Entry je prazen, takoj preveri)
    ime_mat = tk.Label(okno2, text='Vnesi ime matrike:')
    ime_mat.grid(row=1, column=0)
    ime_vnos = tk.Entry(okno2)
    ime_vnos.grid(row=1, column=1)

    def dvofunkcija():
        with open('ime_matrike.txt', 'w') as f:
            f.write(str(ime_vnos.get()))
        okno2.destroy()

    pozdrav_gumb = tk.Button(okno2, text='začni', command=dvofunkcija)
    pozdrav_gumb.grid(row=2, columnspan=2)
    okno2.mainloop()

    ime_txt = open('ime_matrike.txt', 'r')
    ime = ime_txt.read()

    okno = tk.Tk() #okno ki vpraša po obliki matrike
    okno.title('O matriki ' + ime)

    vrsticeA = tk.Label(okno, text='število vrstic matrike ' + ime)
    vrsticeA.grid(row=0, column=0)
    vhodvrst = tk.Entry(okno)
    vhodvrst.grid(row=0, column=1)

    stolpciA = tk.Label(okno, text='število stolpcev matrike ' + ime)
    stolpciA.grid(row=1, column=0)
    vhodstolp = tk.Entry(okno)
    vhodstolp.grid(row=1, column=1)

    def preveri_vrednosti():
        try:    #preveri vrednost velikosti (Naravna števila)
            a1 = int(vhodvrst.get())
            a2 = int(vhodstolp.get())
            def podatki_matrike(): #pobere podatke
                matrikaA = []
                for vrsta in range(a1):
                    vrstica = []
                    for stolpec in range(a2):
                        indeks = (vrsta, stolpec)
                        vrstica.append(vrednost[indeks].get())
                    matrikaA.append(vrstica)
                with open(ime + '.txt', 'w') as f:
                    f.write(str(matrikaA))

            if je_naravno_stevilo(a1): #tu se začne preverjanje
                if je_naravno_stevilo(a2):
                    matrika = tk.Tk()
                    matrika.title('Matrika ' + ime)

                    gumb = tk.Button(matrika, text='poberi podatke', command=podatki_matrike)
                    gumb.grid(row=a1 + 1, column=0)
                    gumb = tk.Button(matrika, text='zapri', command=matrika.destroy)
                    gumb.grid(row=a1 + 1, column=1)
                    okno.destroy()
                    vrednost = {}
                    for vrsta in range(a1): #sestavi matriko
                        for stolpec in range(a2):
                            indeks = (vrsta, stolpec)
                            vhodelement = tk.Entry(matrika)
                            vhodelement.grid(row=vrsta + 1, column=stolpec)
                            vrednost[indeks] = vhodelement
                else:
                    error_okno()
            else:
                error_okno()
        except ValueError:
            error_okno()
    pass

    gumb = tk.Button(okno, text='Začni', command=preveri_vrednosti)
    gumb.grid(row=4, columnspan=2)
    okno.mainloop()
