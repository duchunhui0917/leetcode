class LinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None


link_lists = []
n = int(input())
if n == 1:
    ls = input()
    print(ls)

for i in range(n):
    ls = input()
    link_list = LinkNode(None)
    p = link_list
    for l in ls:
        tmp = LinkNode(l)
        p.next = tmp
        p = tmp
    link_lists.append(link_list.next)

link_list = link_lists[0]
for cur_link_list in link_lists[1:]:
    p = link_list
    q = cur_link_list
    p_data = p.data
    q_data = q.data

    while p is not None and q is not None:
        if q.data > p.data:
            tmp_p = p
            q_next = q.next
            while tmp_p.next and q.data > tmp_p.next.data:
                tmp_p = tmp_p.next
            tmp = tmp_p.next
            tmp_p.next = q
            q.next = tmp

            p = tmp
            q = q_next
        else:
            tmp_q = q
            p_next = p.next
            while tmp_q.next and p.data >= tmp_q.next.data:
                tmp_q = tmp_q.next
            tmp = tmp_q.next
            tmp_q.next = p
            p.next = tmp



