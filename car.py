n, a, b = list(map(int, input().split(' ')))
profits = []
for i in range(n):
    x, y = list(map(int, input().split(' ')))
    profits.append([x, y])
dp = [[[0 for k in range(b + 1)] for j in range(a + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, a):
        dp[i][j][0] = max(dp[i - 1][j - 1][0] + profits[i - 1][0],
                          dp[i - 1][j][0])
    for k in range(1, b):
        dp[i][0][k] = max(dp[i - 1][0][k - 1] + profits[i - 1][1],
                          dp[i - 1][0][k])

for i in range(1, n + 1):
    for j in range(1, a + 1):
        for k in range(1, b + 1):
            dp[i][j][k] = max(dp[i - 1][j - 1][k] + profits[i - 1][0],
                              dp[i - 1][j][k - 1] + profits[i - 1][1],
                              dp[i - 1][j][k])
print(dp[n][a][b])
