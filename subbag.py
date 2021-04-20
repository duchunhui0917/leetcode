def canPartition(nums) -> bool:
    n = len(nums)
    if n == 0 or n == 1:
        return False
    s = sum(nums)
    if s % 2 == 1:
        return False
    else:
        s = s // 2
    dp = [[False for j in range(s + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = True
        for j in range(1, s + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    for i in range(1, n + 1):
        if dp[i][s] == True:
            return True
    return False


n = 5
nums = [30, 60, 5, 15, 30]
res = [i for i in range(n)]
ls = []


def process(l, res):
    if len(res) == 0:
        return
    ls.append(l)
    for i in res:
        nres = res[:]
        nres.remove(i)
        nl = l[:]
        nl.append(i)
        process(nl, nres)


process([], res)
ls.remove([])
ls.sort(key=lambda x: sum(nums[i] for i in x))
for l in ls:
    new_nums = nums[:]

    for i in l:
        new_nums.remove(nums[i])
    if canPartition(new_nums):
        print(sum(nums[i] for i in l))
        break
