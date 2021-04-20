N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int, input().split(' '))))


def get_ij(grid):
    row_sum = []
    for i in range(n):
        row_sum.append(sum(grid[i]))
    column_sum = []
    for j in range(n):
        column_sum.append(sum([grid[i][j] for i in range(n)]))

    max_i = 0
    max_j = 0
    max_val = row_sum[0] + column_sum[0] - grid[0][0]
    for i in range(n):
        for j in range(n):
            val = row_sum[i] + column_sum[j] - grid[i][j]
            if val > max_val:
                max_i = i
                max_j = j
                max_val = val
    return max_i, max_j


n = N
while n != 0:
    i, j = get_ij(grid)
    grid.pop(i)
    for g in grid:
        g.pop(j)
    n -= 1
    print(i + 1, j + 1)
