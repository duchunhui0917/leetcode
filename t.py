s = 'aa bcd edf deda'
words = ['ded']


def dfs(i, offset):
    global s
    for word in words:
        if offset == len(word) - 1:

            if s[i - offset - 1] != ' ':
                s = s[:i - offset - 1] + ' ' + s[i - offset - 1 + 1:]
                i += 1
            for j in range(i - offset, i):
                if s[j] == ' ':
                    s = s[:j] + s[j + 1:]
                    i -= 1
            if s[i] != ' ':
                s = s[:i - offset - 1] + ' ' + s[i - offset - 1 + 1:]
                i += 1
            dfs(i + 1, 0)
        if s[i] == word[offset]:
            dfs(i + 1, offset + 1)
    dfs(i + 1, offset)


dfs(0, 0)
print(s)
