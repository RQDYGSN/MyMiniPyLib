from .Point import *


class Hypersphere:
    def __init__(self, point: Point, radius: (float, int)):
        self.center = point
        self.radius = radius

    def contain(self, point: Point, boundary: bool = True, mode: str = "l2"):
        assert len(point.coordinate) == len(self.center.coordinate)
        if boundary:
            return self.center.distance(point, mode=mode) <= self.radius
        return self.center.distance(point, mode=mode) < self.radius


class Circle(Hypersphere):
    def __init__(self):
        assert len(self.coordinate) == 2

