import pytest
from problems.leetcode.hashmap.contains_duplicate_2 import Solution

@pytest.fixture
def sol():
    return Solution()

class Test_Solution:
    def test_basic(self, sol):
        assert sol.containsNearbyDuplicate([1,2,3,1], 3) == True

    def test_basic2(self, sol):
        assert sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    
    def test_basic3(self, sol):
        assert sol.containsNearbyDuplicate([1,0,1,1], 1) == True
