import pytest
from problems.leetcode.binary_tree_bfs.average_levels_in_binary_tree import Solution, TreeNode
from tests.helpers.build_tree import build_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.averageOfLevels(build_tree([3,9,20,None,None,15,7])) == pytest.approx([3.00000,14.50000,11.00000])

    def test_basic2(self, sol):
        assert sol.averageOfLevels(build_tree([3,9,20,15,7])) == pytest.approx([3.00000,14.50000,11.00000])
    
    def test_basic3(self, sol):
        assert sol.averageOfLevels(build_tree([3,9,20,3,None,15,7])) == pytest.approx([3.00000,14.50000,8.33333])
