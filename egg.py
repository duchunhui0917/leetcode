def superEggDrop(K: int, N: int) -> int:
    def cal(i, j):
        for k in range(1, j + 1):
            dp[i][j] = min(
                dp[i][j],
                max(
                    dp[i][j - k],
                    dp[i - 1][k - 1]
                ) + 1
            )

    dp = [[float('inf') for j in range(N + 1)] for i in range(K + 1)]
    for i in range(K + 1):
        dp[i][0] = 0
    for j in range(N + 1):
        dp[1][j] = j
    for i in range(2, K + 1):
        for j in range(1, N + 1):
            cal(i, j)
    return dp[K][N]


print(superEggDrop(2, 6))
