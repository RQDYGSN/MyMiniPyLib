from .. import MyMiniPy as py

adj = [
    [0, 2, 6, 4],
    [float("inf"), 0, 3, float("inf")],
    [7, float("inf"), 0, 1],
    [5, float("inf"), 12, 0]
]
g = py.graph(adj)
g.print_adjacency()
gg = py.shortestPathClass(g)

class TestGraph:
    def test_graph(self):
        assert gg.shortestPath(1, 0) == [1, 2, 3, 0]
        assert gg.shortestCost(1, 0) == 9
