import pytest
from problems.leetcode.binary_tree_general.invert_binary_tree import Solution
from tests.helpers.build_tree import build_tree
from tests.helpers.level_order_traverse_tree import traverse_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert traverse_tree(sol.invertTree(build_tree([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1]

    def test_basic2(self, sol):
        assert traverse_tree(sol.invertTree(build_tree([2,1,3]))) == [2,3,1]
    
    def test_basic3(self, sol):
        assert traverse_tree(sol.invertTree(build_tree([1]))) == [1]

    def test_basic4(self, sol):
        assert traverse_tree(sol.invertTree(build_tree([]))) == []