import pytest
from problems.leetcode.easy.climbing_stairs import Solution

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.climbStairs(2) == 2

    def test_basic2(self, sol):
        assert sol.climbStairs(3) == 3
    
    def test_basic3(self, sol):
        assert sol.climbStairs(1) == 1