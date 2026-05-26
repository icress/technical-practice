# Date Solved: 2026-05-26
# Difficulty: Medium
# Need to review: True

# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])