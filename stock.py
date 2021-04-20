def maxProfit(k, prices):
    l = len(prices)
    if l == 0:
        return 0
    dp = [[[0 for hh in range(2)] for kk in range(k + 1)] for ll in range(l + 1)]
    for kk in range(k + 1):
        dp[0][kk][1] = - prices[0]
    for ll in range(l + 1):
        dp[ll][0][1] = - prices[0]

    for ll in range(1, l + 1):
        for kk in range(1, k + 1):
            dp[ll][kk][0] = max(
                dp[ll - 1][kk][1] + prices[ll - 1],
                dp[ll - 1][kk][0]
            )
            dp[ll][kk][1] = max(
                dp[ll - 1][kk - 1][0] - prices[ll - 1],
                dp[ll - 1][kk][1]
            )
    return dp[l][k][0]


k = 2
prices = [2, 1, 2, 0, 1]
print(maxProfit(k, prices))
