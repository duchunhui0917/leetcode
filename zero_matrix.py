matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

M = len(matrix)
N = len(matrix[0])

row = [False for _ in range(M)]
column = [False for _ in range(N)]

for m in range(M):
    for n in range(N):
        if matrix[m][n] == 0:
            row[m] = True
            column[n] = True

for m in range(M):
    for n in range(N):
        if row[m] or column[n]:
            matrix[m][n] = 0

print(matrix)
