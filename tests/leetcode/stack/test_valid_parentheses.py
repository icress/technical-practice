import pytest
from problems.leetcode.stack.valid_parentheses import Solution

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.isValid("()") == True

    def test_basic2(self, sol):
        assert sol.isValid("([{}])") == True
    
    def test_basic3(self, sol):
        assert sol.isValid("([)]") == False
    
    def test_only_open(self, sol):
        assert sol.isValid("(") == False

    def test_only_close(self, sol):
        assert sol.isValid("]") == False