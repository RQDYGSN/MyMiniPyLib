class graph:

    def __init__(self, adjacency_matrix):
        assert isinstance(adjacency_matrix, list)
        for i in adjacency_matrix:
            assert isinstance(i, list)
            for j in i:
                assert isinstance(j, (float, int))
        self.adj = adjacency_matrix

    def print_adjacency(self):
        """
        :return: print adjacency matrix.
        """
        print('Graph:')
        for row in self.adj:
            for e in row:
                print('∞' if e == float("+inf") else e, end='\t')
            print()
        return


class shortestPathClass:
    def __init__(self, graph):
        self.__costs = []
        self.__parents = []
        self.__floyedState = 0
        self.adj = graph.adj

    def floyd(self):
        """
        弗洛伊德算法
        assumption: 可以有负权边，但不能有负权环.
        """
        if self.__floyedState == 1:
            return
        import copy
        costs = copy.deepcopy(self.adj)
        parents = [[i] * len(costs) for i in range(len(costs))]  # 关键地方，i-->j 的父结点初始化都为i
        n = len(costs)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if costs[i][k] + costs[k][j] < costs[i][j]:
                        costs[i][j] = costs[i][k] + costs[k][j]
                        parents[i][j] = parents[k][j]
        self.__floyedState = 1
        self.__costs = costs
        self.__parents = parents
        return

    def shortestPath(self, i, j):
        self.floyd()
        ans = [j]
        while self.__parents[i][j] != i:
            j = self.__parents[i][j]
            ans.insert(0, j)
        if len(ans) == 1:
            return ans
        return [i] + ans

    def shortestCost(self, i, j):
        self.floyd()
        while self.__floyedState == 0:
            self.floyd()
        return self.__costs[i][j]

    @staticmethod
    def dijkstra(start: int, adj: list):
        """
        迪杰斯特拉算法
        assumption: 不可以有负权边.
        :param start: index of start node.
        :param adj: adjacency matrix.
        :return: list of shortest distances from node 'start' to all nodes.
        """
        passed = [start]
        nopass = [idx for idx in range(len(adj)) if idx != start]
        dis = adj[start]
        prenode = [-1 for i in range(len(adj))]  # 记录前驱节点，没有则用-1表示
        while len(nopass):
            idx = nopass[0]
            for i in nopass:
                if dis[i] < dis[idx]:
                    idx = i

            nopass.remove(idx)
            passed.append(idx)

            for i in nopass:
                if dis[idx] + adj[idx][i] < dis[i]:
                    dis[i] = dis[idx] + adj[idx][i]
                    prenode[i] = idx
        return dis, prenode

    @staticmethod
    def spfa(start: int, adj: list):
        from queue import Queue
        """
        SPFA算法: Shortest Path Faster Algorithm
        :param adj: adjacency matrix
        :param start: index of start node
        :return: list of shortest distances, list of .
        """
        a = adj
        m, n = len(a), len(a[0])
        count = [0 for i in range(n)]
        dis = [float("inf") for i in range(n)]
        vis = [0 for i in range(n)]
        dis[start] = 0
        vis[start] = 1
        que = Queue()
        prenode = [-1 for i in range(n)]  # 记录前驱节点，没有则用-1表示
        que.put(start)
        while not que.empty():
            v = que.get()
            vis[v] = 0
            for i in range(n):
                temp = dis[v] + a[v][i]
                if dis[i] > temp:
                    dis[i] = temp  # 修改最短路
                    prenode[i] = v
                    if vis[i] == 0:  # 如果扩展节点i不在队列中，入队
                        count[i] += 1
                        if count[i] > n:
                            raise ValueError("输入有负环异常")
                        que.put(i)
                        vis[i] = 1
        return dis, prenode
