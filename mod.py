n = 5
m = 5
ls = [3, 3, 3, 3, 2]
dp = [[False for j in range(m)] for i in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True


for i in range(1, n + 1):
    for j in range(m):
        if ls[i - 1] % m > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j - ls[i - 1] % m] or dp[i - 1][j]
for j in range(m - 1, -1, -1):
    if dp[n][j]:
        print(j)
        break
