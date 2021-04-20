from functools import lru_cache

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def longestIncreasingPath(matrix):
    bias = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        save = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(i, j):
            if save[i][j]:
                return save[i][j]
            save[i][j] = 1
            for dx, dy in DIRS:
                x = i + dx
                y = j + dy
                if 0 <= x < row and 0 <= y < col and matrix[x][y] > matrix[i][j]:
                    save[i][j] = max(save[i][j], dfs(x, y) + 1)
            return save[i][j]

        val = 0
        for i in range(row):
            for j in range(col):
                val = max(val, dfs(i, j))
        return val


matrix = [[9, 1, 4],
          [6, 2, 8],
          [5, 5, 7]]
print(longestIncreasingPath(matrix))
