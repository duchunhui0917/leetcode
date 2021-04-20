def dfs(i, j):
    if board[i][j] == 'T':
        return 0
    if save[i][j]:
        return save[i][j]
    mark[i][j] = True
    bias = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = float('inf')
    for dx, dy in bias:
        x = i + dx
        y = j + dy
        if 0 <= x < M and 0 <= y < N and board[x][y] != '1' and mark[x][y] is False:
            tmp = dfs(x, y) + 1
            if tmp < ans:
                ans = tmp
    mark[i][j] = False
    save[i][j] = min(save[i][j], ans)
    return ans


board = []
M, N = list(map(int, input().split(' ')))
for i in range(M):
    board.append(input())

mark = [[False for _ in range(N)] for _ in range(M)]
save = [[0 for _ in range(N)] for _ in range(M)]

res = float('inf')
locates = []
for m in range(M):
    for n in range(N):
        if board[m][n] == 'X':
            r = dfs(m, n)
            if r < res:
                res = r
                locates = [(m, n)]
            elif r == res:
                locates.append((m, n))
locates.sort(key=lambda x: (x[0], x[1]))
if res == float('inf'):
    print(0)
else:
    print(res)
    for locate in locates:
        print(locate[0], end=' ')
        print(locate[1], end=' ')
