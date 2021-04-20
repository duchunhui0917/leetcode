mask = ['1101', '1010', '1111', '1110']
txt = ['ABCD', 'EFGH', 'IJKL', 'MNPQ']

N = len(mask) - 1
ls = [[]]
for i in range(len(mask)):
    s = mask[i]
    for j in range(len(s)):
        if s[j] == '0':
            ls[0].append((i, j))

for n in range(3):
    tmp = []
    for locate in ls[-1]:
        tmp.append((locate[1], N - locate[0]))
    tmp.sort(key=lambda x: (x[0], x[1]))
    ls.append(tmp)

res = ''
for s in ls:
    for locate in s:
        res += txt[locate[0]][locate[1]]

print(res)





