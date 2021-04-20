class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


M, N = list(map(int, input().split(' ')))
d = {}
for m in range(M):
    d.setdefault(m + 1, [0, 0])
for n in range(N):
    father, locate, child = input().split(' ')
    father = int(father)
    child = int(child)
    if locate == 'left':
        d[father][0] = child
    else:
        d[father][1] = child


def count(root):
    l, r = d[root.val][0], d[root.val][1]
    if l == 0 and r == 0:
        return True, 0
    lf, rf = None, None
    lc, rc = 0, 0
    if l != 0:
        root.left = Node(l)
        lf, lc = count(root.left)
    if r != 0:
        root.right = Node(r)
        rf, rc = count(root.right)
    if lf and rf:
        return False, 1
    else:
        return False, lc + rc


flag, c = count(Node(1))
print(c)
