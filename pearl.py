N = int(input())
ls = []
for n in range(N):
    string = input()
    l = len(string)
    cs = string[0]
    dp = [[0, 0] for i in range(l)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, l):
        if string[i] == string[i - 1]:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            cl0 = 1
            if cl1 + 1 >= dp[i - 1][1]:
                dp[i][1] = cl1 + 1
                cl1 += 1
            else:
                dp[i][1] = dp[i - 1][1]
                cl1 = 1
    ls.append(dp[l-1][1])

for count in ls:
    print(count)

