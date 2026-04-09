import pytest
from problems.leetcode.array_string.length_of_last_word import Solution
from tests.helpers.build_tree import build_tree

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.lengthOfLastWord("Hello World") == 5

    def test_basic2(self, sol):
        assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4
    
    def test_basic3(self, sol):
        assert sol.lengthOfLastWord("luffy is still joyboy") == 6

    def test_basic4(self, sol):
        assert sol.lengthOfLastWord("a ") == 1
