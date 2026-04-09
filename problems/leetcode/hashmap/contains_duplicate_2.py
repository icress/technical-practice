# Date Solved: 2026-04-09
# Difficulty: Easy
# Need to review: False

# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_hash = {}
        for i in range(len(nums)):
            if nums[i] in nums_hash:
                if abs(i - nums_hash[nums[i]]) <= k:
                    return True
            nums_hash[nums[i]] = i
        return False