from .. import minipy as py

numList1 = py.numList([])
numList2 = py.numList([1, 1, 1, 1, 1])
numList3 = py.numList([1, 2, 3, 4, 5])
numList4 = py.numList([5, 1, 3, 2, 4])

class TestnumList:
    def test_findMiddleIndex(self):
        assert numList1.findMiddleIndex() == -1
        assert numList2.findMiddleIndex() == 2
        assert numList3.findMiddleIndex() == -1
        assert numList4.findMiddleIndex() == 2

    def test_minimumDifference(self):
        assert numList1.minimumDifference(2) == -1
        assert numList2.minimumDifference(2) == 0
        assert numList3.minimumDifference(2) == 1
        assert numList4.minimumDifference(2) == 1

    def test_insertionSort(self):
        assert numList1.insertionSort() == []
        assert numList2.insertionSort() == [1, 1, 1, 1, 1]
        assert numList3.insertionSort() == [1, 2, 3, 4, 5]
        assert numList4.insertionSort() == [1, 2, 3, 4, 5]

    def test_mergeSort(self):
        assert numList1.mergeSort() == []
        assert numList2.mergeSort() == [1, 1, 1, 1, 1]
        assert numList3.mergeSort() == [1, 2, 3, 4, 5]
        assert numList4.mergeSort() == [1, 2, 3, 4, 5]
