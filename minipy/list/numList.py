class numList:
    def __init__(self, array):
        for i in array:
            if isinstance(i, int) or isinstance(i, float):
                continue
            else:
                raise Exception("Input object is not a type of numList.")
        self.arr = array

    def findMiddleIndex(self):
        """
        :param self.arr: type list[int], list[float]
        :return:
            The most-left middle index of self.arr that "self.arr[0] + self.arr[1] + ... + self.arr[middleIndex-1] ==
            self.arr[middleIndex+1] + self.arr[middleIndex+2] + ... + self.arr[self.arr.length-1]".
            if success, return the index, else return -1.
        """
        s = sum(self.arr)
        now = 0
        for i in range(len(self.arr)):
            t = s - self.arr[i]
            if t % 2 == 0 and now == t//2:
                return i
            now += self.arr[i]
        return -1

    def minimumDifference(self, k):
        """
        :param k: the number of elements.
        :return:
            Select k elements from self.arr to minimize the difference between the highest and lowest numbers.
            Returns the smallest possible difference.
        """
        if len(self.arr) < k:
            return -1
        nums = sorted(self.arr)
        return min([nums[i+k-1]-nums[i] for i in range(len(nums)-k+1)])

    def insertionSort(self):
        """
        INSERTION-SORT
        :return: sorted self.arr.
        """
        if len(self.arr) < 2:
            return self.arr
        nums = [i for i in self.arr]
        for j in range(1, len(nums)):
            key = nums[j]
            i = j - 1
            while i >= 0 and nums[i] > key:
                nums[i+1] = nums[i]
                i = i - 1
            nums[i+1] = key
        return nums

    def __merge(self, arr, p, q, r):
        """
        :param arr: numList
        :param p: begin index of numList part 1.
        :param q: end index of numList part 1.
        :param r: end index of numList part 2.
        :return: arr that arr[p:q+1:] and arr[q+1:r:] are merged.
        """
        n1 = q - p + 1
        n2 = r - q
        assert n1 >= 0 and n2 >= 0 and p >= 0 and r < len(arr)
        if n1 == 0 or n2 == 0:
            return
        l, r = arr[p:q+1:], arr[q+1:r+1:]
        l.append(float("+inf"))
        r.append(float("+inf"))
        i, j = 0, 0
        pointer = p
        while i < n1 or j < n2:
            if l[i] < r[j]:
                arr[pointer] = l[i]
                i += 1
            else:
                arr[pointer] = r[j]
                j += 1
            pointer += 1
        return

    def __mergeSort(self, nums, begin, end):
        if begin < end:
            mid = begin + (end - begin)//2
            self.__mergeSort(nums, begin, mid)
            self.__mergeSort(nums, mid+1, end)
            self.__merge(nums, begin, mid, end)
        return

    def mergeSort(self):
        nums = [i for i in self.arr]
        self.__mergeSort(nums, 0, len(nums)-1)
        return nums