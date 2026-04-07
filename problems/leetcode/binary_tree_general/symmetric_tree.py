# Date Solved: 2026-04-07
# Difficulty: Easy
# Need to review: True

# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left) and node1.val == node2.val
        
        return isMirror(root.left, root.right)


# First pass solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def bfs(root: TreeNode, level, tree):
#     if len(tree) <= level:
#         tree.append([])

#     if root:
#         tree[level].append(root.val)
#         bfs(root.left, level + 1, tree)
#         bfs(root.right, level + 1, tree)
#     else:
#         tree[level].append(None)
#     return tree

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         tree = bfs(root, 0, [])
#         for level in range(len(tree)):
#             if tree[level] != tree[level][::-1] or len(tree[level]) % 2 != 0 and level != 0:
#                 return False
#         return True

# BAD TIME COMPLEXITY SOLUTION