s1 = "ab"
s2 = "eidbaooo"
need = {}
windows = {}
valid = 0
for s in s1:
    need.setdefault(s, 0)
    windows.setdefault(s, 0)
    need[s] += 1
l = r = 0
while r < len(s2):
    c = s2[r]
    r += 1
    if c in need:
        windows[c] += 1
        if windows[c] == need[c]:
            valid += 1
    while valid == len(need):
        if s2[l] not in 

