def process(i, j):
    if (i, j) == end:
        return 0
    if save[i][j]:
        return save[i][j]
    mark[i][j] = True
    bias = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = float('inf')
    for dx, dy in bias:
        x = i + dx
        y = j + dy
        if 0 <= x < m and 0 <= y < n and board[x][y] != '#' and board[x][y] != '@' and mark[x][y] is False:
            tmp = process(x, y) + 1
            if tmp < ans:
                ans = tmp
    mark[i][j] = False
    return ans


board = [
    ['1', '1', '1'],
    ['1', '#', '#'],
    ['1', '1', '1']
]
m = len(board)
n = len(board[0])
start = (0, 0)
end = (1, 1)

mark = [[False for _ in range(n)] for _ in range(m)]
save = [[0 for _ in range(n)] for _ in range(m)]
res = process(start[0], start[1])
if res != float('inf'):
    print(res)
else:
    print(-1)
