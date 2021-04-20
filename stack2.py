M = int(input())
N = int(input())

dis = []
for n in range(N):
    dis.append(int(input()))
dp = []
for n in range(N + 1):
    d = {}
    d.setdefault('011', 0)
    d.setdefault('101', 0)
    d.setdefault('110', 0)
    d.setdefault('111', 0)
    dp.append(d)

res = -1
for n in range(1, N + 1):
    for k in range(3):
        dp[n][k][0] = max(dp[n-1][k])
        dp[n][k][1] = max(dp[n][k - 1][])
    if max(dp[n].values()) > M:
        res = n
        break
print(res)

