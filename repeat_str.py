s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)
i, j = 0, 0
while i < l1 and j < l2 and s1[i] == s2[j]:
    i += 1
    j += 1
s = s1[:i]

ml = min(l1, l2)
for i in range(1, len(s) + 1):
    flag = True
    j = i
    if ml % i != 0:
        flag = False
    else:
        for j in range(0, ml, i):
            for k in range(i - 1):
                if s1[:j + k] != s2[:j + k]:
                    flag = False
    print(flag)
    if not flag:
        break
    print(flag)

if i == 1:
    print('')
else:
    print(s[:i])
