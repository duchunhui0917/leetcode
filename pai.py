target = 'arcsoft'

T = int(input())
ls = []
for t in range(T):
    N, M = map(int, input().split(' '))
    for m in range(M):
        string, a, b = input().split(' ')
        a = int(a)
        b = int(b)
        lucky = a ** b % 7
        index = 0
        flag = 'no'
        for i, s in enumerate(string):
            if i == lucky or s == target[index]:
                index += 1
                if index == len(target):
                    flag = 'yes'
                    break
            else:
                index = 0
        ls.append(flag)

for l in ls:
    print(l)
