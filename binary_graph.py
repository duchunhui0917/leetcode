# 匈牙利算法（dfs）
class Hungarian:

    def search_extend_path(self, l_node, adjoin_map, l_match, r_match, visited_set):
        '''深度搜索增广路径'''
        for r_node in adjoin_map[l_node]:  # 邻接节点
            if r_node not in r_match.keys():  # 情况1： 未匹配, 则找到增广路径，取反
                l_match[l_node] = r_node
                r_match[r_node] = l_node
                return True
            else:  # 情况2：　已匹配
                next_l_node = r_match[r_node]
                if next_l_node not in visited_set:
                    visited_set.add(next_l_node)
                    if self.search_extend_path(next_l_node, adjoin_map, l_match, r_match, visited_set):  # 找到增广路径，取反
                        l_match[l_node] = r_node
                        r_match[r_node] = l_node
                        return True
                return False

    def run(self, adjoin_map):
        '''
        :param adjoin_map: {x_i: [y_j, y_k]}
        :return:
        '''
        l_match, r_match = {}, {}  # 存放匹配
        for lNode in adjoin_map.keys():
            self.search_extend_path(lNode, adjoin_map, l_match, r_match, set())
        return l_match


males = list(map(int, input().split(' ')))
females = list(map(int, input().split(' ')))
N = int(input())
d = {}
for n in range(N):
    m, f = list(map(int, input().split(' ')))
    if m not in d:
        d[m] = [f]
    else:
        d[m].append(f)
print(Hungarian().run(d))
print(len(Hungarian().run(d)))
