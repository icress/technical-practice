import pytest
from problems.leetcode.intervals.summary_ranges import Solution

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]

    def test_basic2(self, sol):
        assert sol.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]