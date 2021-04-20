N, M, K = map(int, input().split(' '))
ls = []
for i in range(N):
    price, weight, v = map(int, input().split(' '))
    ls.append((price, weight, v))
ls.sort(key=lambda x: (x[2], x[0]))

dp = [[[0 for p in range(K)]for w in range(M)]for n in range(N)]

for n in range(N):
    for w in range(M):
        for p in range(K):
            cp = ls[n][0]
            cw = ls[n][1]
            if cp < p and cw < w:
                dp[n][w][p] = max(dp[n][w][p], dp[n][w - cw][p - cp] + 1)
print()
