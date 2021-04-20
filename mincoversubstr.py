def minWindow():
    need = {}
    windows = {}
    for tt in t:
        windows.setdefault(tt, 0)
        need.setdefault(tt, 0)
        need[tt] += 1
    valid = 0
    start = l = r = 0
    length = len(s)
    while r < len(s):
        c = s[r]
        r += 1
        if c in t:
            windows[c] += 1
            if windows[c] == need[c]:
                valid += 1
        while valid == len(need):
            if r - l < length:
                start = l
                length = r - l
            c = s[l]
            if c in need:
                if windows[c] == need[c]:
                    break
                else:
                    windows[c] -= 1
                    l += 1

            else:
                l += 1

    return s[start:start + length] if valid == len(need) else ''


s = "cabwefgewcwaefgcf"
t = "cae"
print(minWindow())
