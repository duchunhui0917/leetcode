g = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]

R = len(g)
C = len(g[0])
dp = [[[float('inf'), float('inf')] for _ in range(C + 1)] for _ in range(R + 1)]

for r in range(1, R + 1):
    for c in range(1, C + 1):
        if r == 1 and c == 1:
            dp[r][c][0] = dp[r][c][1] = 1 - g[0][0]
        else:
            if dp[r][c - 1][1] < dp[r - 1][c][1]:
                dp[r][c][0] = dp[r][c - 1][0] - g[r - 1][c - 1]
                dp[r][c][1] = max(dp[r][c][0], dp[r][c - 1][1])
            else:
                dp[r][c][0] = dp[r - 1][c][0] - g[r - 1][c - 1]
                dp[r][c][1] = max(dp[r][c][0], dp[r - 1][c][1])

print(dp[R][C][1])
