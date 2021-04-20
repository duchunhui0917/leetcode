def dfs(i, j, w):
    if save[i][j]:
        return save[i][j]

    if w == len(word) - 1:
        save[i][j] = 1
        return 1

    bias = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in bias:
        x = i + dx
        y = j + dy
        if 0 <= x < row and 0 <= y < col and matrix[x][y] == word[w + 1]:
            save[i][j] += dfs(x, y, w + 1)
    return save[i][j]


matrix = [['C', 'H', 'I', 'A'],
          ['C', 'A', 'N', 'T'],
          ['G', 'R', 'A', 'C'],
          ['B', 'B', 'D', 'E']]
word = 'CHINA'

row = len(matrix)
col = len(matrix[0])
save = [[0 for j in range(col)] for i in range(row)]

val = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == word[0]:
            dfs(i, j, 0)
            val = max(val, save[i][j])
print(val)
