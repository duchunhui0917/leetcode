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
    dp[n]['011'] = dp[n-1]['101'] + dis[n - 1]
    dp[n]['101'] = dp[n-1]['110'] + dis[n - 1]
    dp[n]['110'] = max(dp[n-1]['011'], dp[n-1]['111'])
    dp[n]['111'] = dp[n-1]['011'] + dis[n - 1]
    if max(dp[n].values()) > M:
        res = n
        break
print(res)

