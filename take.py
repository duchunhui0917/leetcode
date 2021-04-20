N = int(input())
dp = [0 for _ in range(N + 1)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    for j in range(1, 4):
        dp[i] = max(dp[i], 0.5 * (1 - dp[i - j]) + 0.5 *(1 - dp[i - j - 1]))
print(dp[N])
