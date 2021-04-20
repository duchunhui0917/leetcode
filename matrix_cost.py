M, N = map(int, input().split(' '))
matrix = []
for m in range(M):
    ls = list(map(int, input().split(' ')))
    matrix.append(ls)

dp = [[float('inf') for n in range(N)] for m in range(M)]
for n in range(N):
    dp[M - 1][n] = matrix[M - 1][n]
bias = [[0, 1], [0, -1], [1, 0]]

flag = [[False for n in range(N)] for m in range(M)]


def dfs(i, j, s):
    c[x][y] = s
    flag[i][j] = True

    for b in bias:
        x = i + b[0]
        y = j + b[1]
        c = abs(data[i][j] - data[x][y])
        if 0 <= x < M and 0 <= y < N and flag[x][y] is False and s + c < c[x][y]:
            dfs(x, y, s + c)
    flag[i][j] = False

    return dp[i][j]


cost = float('inf')
for n in range(N):
    cost = min(dfs(0, n), cost)
print(cost)
