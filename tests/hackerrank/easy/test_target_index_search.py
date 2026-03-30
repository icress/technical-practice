from problems.hackerrank.easy.target_index_search import binarySearch

class Test_Solution:
    def test_basic(self):
        assert binarySearch([1, 2, 3, 4, 5], 3) == 2

    def test_basic2(self):
        assert binarySearch([2, 4, 6, 8, 10, 12, 14, 16], 16) == 7