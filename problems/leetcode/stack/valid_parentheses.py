# Date Solved: 2026-04-02
# Difficulty: Easy
# Need to review: False

# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        keys = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for symbol in s:
            if symbol in keys.keys():
                stack.append(symbol)
            else:
                if not stack:
                    return False
                elif keys[stack[-1]] != symbol:
                    return False
                else:
                    stack.pop()
        return stack == []
                