M=[]
class DFS_hungary():

    def __init__(self, nx, ny, edge, cx, cy, visited):
        self.nx, self.ny=nx, ny
        self.edge = edge
        self.cx, self.cy=cx,cy
        self.visited=visited

    def max_match(self):
        res=0
        for i in self.nx:
            if self.cx[i]==-1:
                for key in self.ny:         # 将visited置0表示未访问过
                    self.visited[key]=0
                res+=self.path(i)
        return res

    def path(self, u):
        for v in self.ny:
            if self.edge[u][v] and (not self.visited[v]):
                self.visited[v]=1
                if self.cy[v]==-1:
                    self.cx[u] = v
                    self.cy[v] = u
                    M.append((u,v))
                    return 1
                else:
                    M.remove((self.cy[v], v))
                    if self.path(self.cy[v]):
                        self.cx[u] = v
                        self.cy[v] = u
                        M.append((u, v))
                        return 1
        return 0

if __name__ == '__main__':
    nx, ny = [0, 1, 2], [3, 4]
    edge = {0:{3: 1, 4: 0},1:{3: 1, 4: 1},0:{3: 1, 4: 1} } # 1 表示可以匹配， 0 表示不能匹配
    cx, cy = {'A':-1,'B':-1,'C':-1,'D':-1}, {'E':-1,'F':-1,'G':-1,'H':-1}
    visited = {'E': 0, 'F': 0, 'G': 0,'H':0}

    print(DFS_hungary(nx, ny, edge, cx, cy, visited).max_match())