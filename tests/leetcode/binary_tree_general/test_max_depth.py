import pytest
from problems.leetcode.binary_tree_general.max_depth import Solution
from tests.helpers.build_tree import build_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.maxDepth(build_tree([3,9,20,None,None,15,7])) == 3

    def test_basic2(self, sol):
        assert sol.maxDepth(build_tree([1,None,2])) == 2
    
    def test_basic3(self, sol):
        assert sol.maxDepth(build_tree([1])) == 1

    def test_basic4(self, sol):
        assert sol.maxDepth(build_tree([])) == 0