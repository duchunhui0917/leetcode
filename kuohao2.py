string = input()
stack = []
d = {}
d.setdefault('(', 0)
d.setdefault('[', 0)

n = 0
for s in string:
    if s == '(':
        stack.append('(')
        d['('] += 1
        n += 1
    if s == ')':
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop(-1)
            n -= 1
        else:
            stack.append(')')
            if d['('] > 0:
                d['('] -= 1
            else:
                n += 1
    if s == '[':
        stack.append('[')
        d['['] += 1
        n += 1
    if s == ']':
        if len(stack) != 0 and stack[-1] == '[':
            stack.pop(-1)
            n -= 1
        else:
            stack.append(']')
            if d['['] > 0:
                d['['] -= 1
            else:
                n += 1

print(n)
