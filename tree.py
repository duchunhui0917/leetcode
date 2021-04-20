ls = [[1, 2, [2]], [2, 3, []]]
worker = 2
d = {}
for s in ls:
    d[s[0]] = [s[1], s[2]]


def process(i):
    res = d[i][0]
    for child in d[i][1]:
        res += process(child)
    return res


print(process(worker))
