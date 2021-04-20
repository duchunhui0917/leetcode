def method(nums):
    sumnum = sum(nums)
    avg = sumnum // 4
    # print(avg)
    sub = 0
    for i in range(avg, -1, -1):    # 这部分遍历可以二分实现，降低复杂度
        sub = 0
        for item in nums:
            if item > i:
                sub += (item - i)

        # print(sub, "sub")
        count = 0
        for item in nums:
            if i>item:
                count += (i - item)*2
        if sub == count:
            return i
        # print(count, "count")
    return -1


if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    nums.sort()
    res = method(nums)
    if res == -1:
        print(res)
    else:
        print(res*4)