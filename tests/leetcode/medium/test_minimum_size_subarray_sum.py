import pytest
from problems.leetcode.medium.minimum_size_subarray_sum import Solution

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.minSubArrayLen(7, [2,3,1,2,4,3]) == 2

    def test_basic2(self, sol):
        assert sol.minSubArrayLen(4, [1,4,4]) == 1
    
    def test_basic3(self, sol):
        assert sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1,1,1]) == 0