m, n = list(map(int, input().split(' ')))
mini = min(m, n)
a = [[0 for j in range(n)] for i in range(m)]
val = 1
for i in range(m):
    mm = min(mini, i)
    for j in range(i, -1, -1):
        a[][j - i] = val
        val += 1
