n, m = list(map(int, input().split(',')))
ls = [x for x in range(n)]
del_number = (m - 1) % n
for i in range(n - 1):
    del ls[del_number]
    del_number = (del_number + m - 1) % len(ls)
print(ls[0])