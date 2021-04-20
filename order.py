def union(p, q):
    global count
    pp = find(p)
    pq = find(q)
    if pp == pq:
        return
    if size[pp] < size[pq]:
        parent[pp] = parent[pq]
        count -= 1
        size[parent[pq]] += size[parent[pp]]
    else:
        parent[pq] = parent[pp]
        count -= 1
        size[parent[pp]] += size[parent[pq]]


def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


n = 5
ls = [(1, 2), (2, 2), (3, 1), (4, 2), (5, 4)]
count = n
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]
for p, q in ls:
    union(p, q)
d = {}

for i in range(1, n + 1):
    if parent[i] not in d:
        d[parent[i]] = [i]
    else:
        d[parent[i]].append(i)
for k in d:
    print(k)
    tmp = d[k][0]
    d[tmp] = d.pop(k)

print(d)
