def process(l, r):
    if r <= l:
        return
    left = l
    right = r
    pivot = ls[left]
    location = left
    while left != right:
        while right > left and ls[right] >= pivot:
            right -= 1
        ls[location] = ls[right]
        location = right
        while right > left and ls[left] <= pivot:
            left += 1
        ls[location] = ls[left]
        location = left
    ls[location] = pivot
    process(l, location - 1)
    process(location + 1, r)


def quick_sort():
    left = 0
    right = len(ls) - 1
    process(left, right)
    [print(ls[i]) for i in range(len(ls))]


ls = [4, 1, 5, 6, 1, 0, 9]
quick_sort()
