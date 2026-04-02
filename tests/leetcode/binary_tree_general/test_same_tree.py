import pytest
from problems.leetcode.binary_tree_general.same_tree import Solution
from tests.helpers.build_tree import build_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.isSameTree(build_tree([1,2,3]), build_tree([1,2,3])) == True

    def test_basic2(self, sol):
        assert sol.isSameTree(build_tree([1,2]), build_tree([1,None,2])) == False
    
    def test_basic3(self, sol):
        assert sol.isSameTree(build_tree([1,2,1]), build_tree([1,1,2])) == False