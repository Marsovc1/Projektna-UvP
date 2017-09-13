import tkinter as tk

def izpis_rezultata(mat):
    okno = tk.Tk()
    rezultat = tk.Label(okno, text=mat, font=('Arial', 20), justify='center')
    rezultat.grid()

    okno.mainloop()

def nicelna_matrika(st_vrstic, st_stolpcev):
    C = []
    for i in range(st_vrstic):
        C.append([])
    for vrstica in range(len(C)):
        for i in range(st_stolpcev):
            C[vrstica].append(0)
    return C

def identicna_matrika(st_vrstic, st_stolpcev):
    I = []
    for i in range(st_vrstic):
        I.append([])
    for vrstica in range(len(I)):
        for stolpec in range(st_stolpcev):
            if vrstica == stolpec:
                I[vrstica].append(1)
            else:
                I[vrstica].append(0)
    return I

def primernost_matrik(matA, matB):
    j = 0
    if len(matA) != len(matB):
        return False
    else:
        for i in range(len(matA)):
            if len(matA[i]) != len(matB[i]):
                j += 1
            elif not all(isinstance(k, (int, float, complex)) for k in matA[i]):
                j += 1
            elif not all(isinstance(k, (int, float, complex)) for k in matB[i]):
                j += 1
        if j == 0:
            return True
        else:
            return False

def seštevalec_matrik(matA, matB):
    if primernost_matrik(matA, matB):
        a = len(matA)
        b = len(matA[0])
        C = nicelna_matrika(a, b)
        for i in range(len(matA)):
            for j in range(len(matA[0])):
                C[i][j] = matA[i][j] + matB[i][j]
        with open('matrika_rezultat.txt', 'w') as f:
            f.write(str(C))
        izpis_rezultata(C)

    else:
        okno = tk.Tk()
        pozor = tk.Label(okno, text='Matriki nista primerni za seštevanje', font=('Arial', 20))
        pozor.grid()
        okno.mainloop()

def odštevalec_matrik(matA, matB):
    if primernost_matrik(matA, matB):
        a = len(matA)
        b = len(matA[0])
        C = nicelna_matrika(a, b)
        for i in range(len(matA)):
            for j in range(len(matA[0])):
                C[i][j] = matA[i][j] - matB[i][j]
        with open('matrika_rezultat.txt', 'w') as f:
            f.write(str(C))
        izpis_rezultata(C)

    else:
        okno = tk.Tk()
        pozor = tk.Label(okno, text='Matriki nista primerni za odštevanje', font=('Arial', 20))
        pozor.grid()
        okno.mainloop()