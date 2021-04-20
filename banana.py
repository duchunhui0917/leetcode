import math


def fit(k):
    s = 0
    for pile in piles:
        s += math.ceil(pile / k)
    return True if s <= H else False


piles = [30, 11, 23, 4, 20]
H = 6
mp = max(piles)
l = 1
h = mp
while l < h:
    k = (l + h) // 2
    if fit(k):
        h = k
    else:
        l = k + 1

print(l)
