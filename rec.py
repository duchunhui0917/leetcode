def MaxSubarray(nums):
    max_sum = cur_sum = nums[0]
    cur_ls = [nums[0]]
    max_ls = cur_ls[:]
    for num in nums[1:]:
        if cur_sum + num > num:
            cur_sum = cur_sum + num
            cur_ls.append(num)
        else:
            cur_sum = num
            cur_ls = [num]
        if cur_sum > max_sum:
            max_ls = cur_ls[:]
            max_sum = cur_sum
    return max_ls


if __name__ == '__main__':
    nums = [1, -2, 3, 5, -2, 6, -1]
    print(MaxSubarray(nums))
