def spiralOrder(n, ls):
    rows, columns = n, n
    visited = [[False] * columns for _ in range(rows)]
    total = rows * columns
    order = [0] * total

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row, column = 0, 0
    directionIndex = 0
    for i in range(total):
        visited[row][column] = ls[i]
        nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
        if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
            directionIndex = (directionIndex + 1) % 4
        row += directions[directionIndex][0]
        column += directions[directionIndex][1]

    for v in visited:
        for i in range(len(v) - 1):
            print(v[i], end=' ')
        print(v[-1])


def fb(n):
    ls = [1, 1]
    for i in range(2, n * n):
        ls.append(ls[i - 1] + ls[i - 2])
    ls = ls[::-1]
    return ls


n = int(input())
ls = fb(n)
spiralOrder(n, ls)
