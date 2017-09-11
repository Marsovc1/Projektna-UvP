a = 1, 11, 2, 3


A = [[1, 1], [2, 2]]
B = [[0, 2], [1, 1]]
C = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]

for r in C:
    print(r)
