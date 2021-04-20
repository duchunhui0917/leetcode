class Node:
    def __init__(self, val, order):
        self.val = val
        self.order = order
        self.left = None
        self.right = None


def build(root, val, order):
    if root is None:
        return Node(val, order)
    if val > root.val:
        root.right = build(root.right, val, order)
    else:
        root.left = build(root.left, val, order)
    return root


def search(root, salary):
    if salary < root.val:
        if root.left is None:
            return -1, -1
        else:
            return search(root.left, salary)
    else:
        if root.right is None:
            return root.val, root.order
        else:
            if salary < root.right.val:
                return root.val, root.order
            else:
                return search(root.right, salary)


res = []
T = int(input())
for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    Q = int(input())
    salaries = []
    for q in range(Q):
        salary = list(map(int, input().split()))
        product = 1
        for s in salary:
            product *= s
        salaries.append(product)

    tree = None
    for index, price in enumerate(prices):
        tree = build(tree, price, index + 1)
    for salary in salaries:
        val, order = search(tree, salary)
        if val == -1:
            res.append((-1, -1))
        else:
            res.append((order, val))

for r in res:
    if r[0] == -1:
        print(-1)
    else:
        print(r[0], end=' ')
        print(r[1])
