# Date Solved: 2026-04-09
# Difficulty: Easy
# Need to review: False

# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i in range(len(nums)):
            if nums[i] in num_hash:
                return [num_hash[nums[i]], i]
            remainder = target - nums[i]
            num_hash[remainder] = i