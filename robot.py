direct = [(0, -1), (1, 0), (0, 1), (-1, 0)]
all_ls = []
T = int(input())
for t in range(T):
    cur = 0
    x = 0
    y = 0
    ls = []
    N, M = map(int, input().split(' '))
    for m in range(M):
        c = input().split(' ')
        if len(c) == 1:
            if c[0] == 'L':
                cur = (cur - 1) % 4
            if c[0] == 'R':
                cur = (cur + 1) % 4
            if c[0] == 'P':
                ls.append([x, y])
        elif len(c) == 2:
            distance = int(c[1])
            if direct[cur][0] == 1:
                x = min(x + distance, N - 1)
            if direct[cur][0] == -1:
                x = max(x - distance, 0)
            if direct[cur][1] == 1:
                y = min(y + distance, N - 1)
            if direct[cur][1] == -1:
                y = max(y - distance, 0)
    all_ls.append(ls)

for i, ls in enumerate(all_ls):
    print('Case #%d' % i)
    for p in ls:
        x = p[0]
        y = p[1]
        print(x, y)
