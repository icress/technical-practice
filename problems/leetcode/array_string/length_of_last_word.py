# Date Solved: 2026-04-09
# Difficulty: Easy
# Need to review: False

# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_and_spaces = s.split(" ")
        words = [w for w in words_and_spaces if w != '']
        if len(words) == 1:
            return len(words[0])
        for i in range(1, len(words)):
            word_length = len(words[-i])
            if word_length > 0:
                return word_length