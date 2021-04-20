class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def creat_tree(fr, mr):
    global num_leaves
    if len(fr) == 0:
        return None
    if len(fr) == 1:
        num_leaves += 1
    root_val = fr[0]
    root = Node(root_val)
    locate = mr.index(root_val)
    root.left = creat_tree(fr[1:1 + locate], mr[:locate])
    root.right = creat_tree(fr[1 + locate:], mr[locate + 1:])
    return root


# def count_leaf(root):
#     global num_leaves
#     if root.left is None and root.right is None:
#         num_leaves += 1
#     if root.left is not None:
#         count_leaf(root.left)
#     if root.right is not None:
#         count_leaf(root.right)


# first_root = ['a', 'b', 'd', 'g', 'c', 'e', 'f', 'h']
# mid_root = ['d', 'g', 'b', 'a', 'e', 'c', 'h', 'f']
first_root = [1, 3, 4]
mid_root = [3, 1, 4]
num_leaves = 0
root = creat_tree(first_root, mid_root)

# count_leaf(root)
print(num_leaves)
