"""
##****
##****
******
******
******
******
"""
N = 6
graph = []
for i in range(N):
    g = list(input())
    graph.append(g)
graph.insert(0, ['*' for _ in range(N)])
for g in graph:
    g.insert(0, '*')

dp = [[1 for j in range(N + 1)]for i in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = dp[i - 1][N]
    for j in range(1, N + 1):
        if graph[i][j] == '*':
            dp[i][j] = dp[i][j - 1]
        else:
            if graph[i - 1][j] == '*' and graph[i][j - 1] == '*':
                dp[i][j] = dp[i][j - 1] * 6
            elif graph[i - 1][j] == '#' and graph[i][j - 1] == '#':
                dp[i][j] = dp[i][j - 1] * 4 + dp[i - 1][j - 1] * 5
            else:
                dp[i][j] = dp[i][j - 1] * 5
print(dp[N][N])
