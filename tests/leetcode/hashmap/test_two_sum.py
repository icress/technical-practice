import pytest
from problems.leetcode.hashmap.two_sum import Solution
from tests.helpers.build_tree import build_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.twoSum([2,7,11,15], 9) == [0,1]

    def test_basic2(self, sol):
        assert sol.twoSum([3,2,4], 6) == [1,2]
    
    def test_basic3(self, sol):
        assert sol.twoSum([3,3], 6) == [0,1]
