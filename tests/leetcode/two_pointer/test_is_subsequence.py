import pytest
from problems.leetcode.two_pointer.is_subsequence import Solution

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.isSubsequence('abc', 'ahbgdc') == True

    def test_basic2(self, sol):
        assert sol.isSubsequence('axc', 'ahbgdc') == False
    
    def test_basic3(self, sol):
        assert sol.isSubsequence('aaaaaa', 'bbaaaa') == False