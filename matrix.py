import math

ls = list(map(int, input().split(' ')))
n, m, k = ls[0], ls[1], ls[2]
matrix = [[i * j for j in range(1, m + 1)] for i in range(1, n + 1)]


def process(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    low = min(n, m)
    if k > low:
        matrix = [row[1:] for row in matrix[1:]]
        val = process(matrix, k - low)
    else:
        if m > n:
            return matrix[0][k - 1]
        else:
            return matrix[k - 1][0]
    return val


print(process(matrix, k))
