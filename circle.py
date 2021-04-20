
radius = 1
x = 1
y = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1

dist = 0
if x < x1 or x > x2:
    dist += min((x1 - x) * (x1 - x), (x2 - x) * (x2 - x))
if y < y1 or y > y2:
    dist += min((y1 - y) * (y1 - y), (y2 - y) * (y2 - y))

print(dist <= radius * radius)
