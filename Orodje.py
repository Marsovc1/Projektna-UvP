

def nicelna_matrika(st_vrstic, st_stolpcev):
    C = []
    for i in range(st_vrstic):
        C.append([])
    for vrstica in range(len(C)):
        for i in range(st_stolpcev):
            C[vrstica].append(0)
    print(C)
nicelna_matrika(3, 5)

def seštevanje_matrika(matA, matB):
    nicelna_matrika(a, b)
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            C[i][j] = matA[i][j] + matB[i][j]
    print(C)