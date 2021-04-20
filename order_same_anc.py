class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
N = int(input())
nodes = []
for n in range(N):
    nodes.append(Node(n))
pairs = []
for n in range(N-1):
    pairs.append(list(map(int, input().split(' '))))
degrees = list(map(int, input().split(' ')))
d = {}
for index, degree in enumerate(degrees):
    if degree not in degree:
        d[degree] = [index]
    else:
        d[degree].append(index)
max_degree = max(d.keys())
for degree in range(max_degree):
    if degree in d:
        

Q = int(input())
