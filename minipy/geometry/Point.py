import math


class Point:
    def __init__(self, coordinate: tuple):
        assert len(coordinate) > 0
        for i in coordinate:
            assert isinstance(i, (float, int))
        self.coordinate = coordinate

    def distance(self, point, mode: str = "l2"):
        return distance(self, point, mode)


class Point2D(Point):
    def __init__(self, coordinate: tuple):
        assert len(coordinate) == 2
        for i in coordinate:
            assert isinstance(i, (float, int))
        self.coordinate = coordinate


def distance(p1: Point, p2: Point, mode: str = "l2"):
    assert len(p1.coordinate) == len(p2.coordinate)
    if mode == "l2":
        return math.sqrt(sum([(p1.coordinate[i] - p2.coordinate[i])**2 for i in range(len(p1.coordinate))]))
    raise Exception("Invalid mode.")
