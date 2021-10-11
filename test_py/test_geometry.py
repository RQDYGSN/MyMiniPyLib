import math
from .. import minipy as py

p11 = py.Point2D(tuple([1, 2]))
p12 = py.Point2D(tuple([-2, -2]))
p21 = py.Point2D(tuple([0, 0]))
p22 = py.Point2D(tuple([1, 1]))
p31 = py.Point2D(tuple([0, 0]))
p32 = py.Point2D(tuple([10, 0]))
p41 = py.Point2D(tuple([20, 21]))
p42 = py.Point2D(tuple([20, 21]))

c1 = py.Hypersphere(py.Point2D(tuple([0, 0])), 0)
c2 = py.Hypersphere(py.Point2D(tuple([0, 0])), 2)
c3 = py.Hypersphere(py.Point2D(tuple([2, 2])), 2*math.sqrt(2))

class TestGeometry:
    def test_distance(self):
        assert py.distance(p11, p12) == 5
        assert py.distance(p21, p22) == math.sqrt(2)
        assert py.distance(p31, p32) == 10
        assert py.distance(p41, p42) == 0

    def test_contain(self):
        assert c1.contain(py.Point2D(tuple([0, 0])), boundary=True, mode="l2")
        assert not c1.contain(py.Point2D(tuple([0, 0])), boundary=False, mode="l2")
        assert c2.contain(py.Point2D(tuple([1, 0])), boundary=True, mode="l2")
        assert not c2.contain(py.Point2D(tuple([-3, 0])), boundary=True, mode="l2")
        assert c3.contain(py.Point2D(tuple([0, 0])), boundary=True, mode="l2")
        assert not c3.contain(py.Point2D(tuple([0, 0])), boundary=False, mode="l2")