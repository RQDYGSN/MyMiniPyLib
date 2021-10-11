"""
main
"""
import minipy as py
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adj = [
        [0, 2, 6, 4],
        [float("inf"), 0, 3, float("inf")],
        [7, float("inf"), 0, 1],
        [5, float("inf"), 12, 0]
    ]
    g = py.graph(adj)
    g.print_adjacency()
    gg = py.shortestPathClass(g)
    print(gg.shortestPath(1, 0))
    print(gg.shortestCost(1, 0))
    print()

    numList1 = py.numList([])
    numList2 = py.numList([1, 1, 1, 1, 1])
    numList3 = py.numList([1, 2, 3, 4, 5])
    numList4 = py.numList([5, 1, 3, 2, 4])
    print(numList1.findMiddleIndex())
    print(numList1.minimumDifference(2))
    print(numList1.insertionSort())
    print(numList1.mergeSort())
    print(numList2.findMiddleIndex())
    print(numList2.minimumDifference(2))
    print(numList2.insertionSort())
    print(numList2.mergeSort())
    print(numList3.findMiddleIndex())
    print(numList3.minimumDifference(2))
    print(numList3.insertionSort())
    print(numList3.mergeSort())
    print(numList4.findMiddleIndex())
    print(numList4.minimumDifference(2))
    print(numList4.insertionSort())
    print(numList4.mergeSort())
    print()

    a = np.array([1, 2, 3])
    print(1, a.dot(a))
    print(2, np.dot(a, a))
    print(3, np.core.dot(a, a))
    print(4, np.core.multiarray.dot(a, a))
    print()

    s = ""
    ss = py.SingleString(s)
    print('max power is', ss.maxPower())
    print()

    point1 = tuple([1, 2])
    point2 = tuple([-2, -2])
    p1 = py.Point2D(point1)
    p2 = py.Point2D(point2)
    print("p1 coordinate is", p1.coordinate)
    print("p2 coordinate is", p2.coordinate)
    print("Distance between p1 and p2 is", py.distance(p1, p2))
