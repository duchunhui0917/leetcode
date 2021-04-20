N, M = map(int, input().split(' '))
cs = []
vs = []
for i in range(N):
    c, v = map(int, input().split(' '))
    cs.append(c)
    vs.append(v)
min_c = min(min(cs), 0)

dp = [float('-inf') for i in range(M + min_c + 1)]
dp[0] = 0
for i in range(N):
    for c, v in zip(cs, vs):
        c -= min_c
        for j in range(M + min_c):
            if j >= c:
                dp[j] = max(dp[j], dp[j - c] + v)
print(dp)
print(dp[-1])
