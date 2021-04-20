N, M, T = (int(i) for i in input().split())

goods0 = []
for i in range(N):
    goods0.append([int(j) for j in input().split()])
goods1 = []
for i in range(M):
    goods1.append([int(j) for j in input().split()])

max_nice0 = max([good[1] for good in goods0])
max_nice1 = max([good[1] for good in goods1])
max_nice = max_nice0 + max_nice1

hot = [0 for i in range(max_nice + 1)]
for nice in range(1, max_nice + 1):
    for good in goods0:
        if nice <= good[1]:
            hot[nice] = good[0]
        else:
            hot[nice] = min(hot[nice], hot[nice - good[1]] + good[0])
for nice in range(max_nice + 1):
    for good in goods1:
        if nice <= good[1]:
            hot[nice] = good[0]
        else:
            hot[nice] = min(hot[nice], hot[nice - good[1]] + good[0])
min_hot = min(hot[T:])

if max_nice < T:
    print(-1)
else:
    print(min_hot)

