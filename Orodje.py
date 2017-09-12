a = [[2, 2], [2, 2]]
b = [[1, 1], [0, 0]]

def nicelna_matrika(st_vrstic, st_stolpcev):
    C = []
    for i in range(st_vrstic):
        C.append([])
    for vrstica in range(len(C)):
        for i in range(st_stolpcev):
            C[vrstica].append(0)
    return C

def primernost_matrik(matA, matB):
    j = 0
    if len(matA) != len(matB):
        return False
    else:
        for i in range(len(matA)):
            if len(matA[i]) != len(matB[i]):
                j += 1
        if j == 0:
            return True
        else:
            return False

def seštevalec_matrik(matA, matB):
    if primernost_matrik(matA, matB) == True:
        a = len(matA)
        b = len(matA[0])
        C = nicelna_matrika(a, b)
        for i in range(len(matA)):
            for j in range(len(matA[0])):
                C[i][j] = matA[i][j] + matB[i][j]
        print(C)
    else:
        print('matriki nista primerni za seštevanje')

def odštevalec_matrik(matA, matB):
    if primernost_matrik(matA, matB) == True:
        a = len(matA)
        b = len(matA[0])
        C = nicelna_matrika(a, b)
        for i in range(len(matA)):
            for j in range(len(matA[0])):
                C[i][j] = matA[i][j] - matB[i][j]
        print(C)
    else:
        print('matriki nista primerni za odštevanje')