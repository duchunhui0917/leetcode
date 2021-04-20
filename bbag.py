n, y = list(map(int, input().split(' ')))

m = {}
for i in range(n):
    x, hp = list(map(int, input().split(' ')))
    m[x] = hp

count = 0
for item in m.keys():
    x = m[item]
    if x > 0:
        for other in m.keys():
            if other <= item + 2 * y:
                m[other] = m[other] - x
        count += x
print(count)
