import pytest
from problems.leetcode.binary_tree_general.symmetric_tree import Solution
from tests.helpers.build_tree import build_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.isSymmetric(build_tree([1,2,3])) == False

    def test_basic2(self, sol):
        assert sol.isSymmetric(build_tree([1,2,2])) == True
    
    def test_basic3(self, sol):
        assert sol.isSymmetric(build_tree([1,2,2,3,4,4,3])) == True