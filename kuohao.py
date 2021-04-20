string = input()
d = {}
d.setdefault('(', 0)
d.setdefault(')', 0)
d.setdefault('[', 0)
d.setdefault(']', 0)

for s in string:
    if s == '(':
        d['('] += 1
    if s == ')':
        if d['('] > 0:
            d['('] -= 1
        else:
            d[')'] += 1
    if s == '[':
        d['['] += 1
    if s == ']':
        if d['['] > 0:
            d['['] -= 1
        else:
            d[']'] += 1

res = 0
for val in d.values():
    res += val
print(res)