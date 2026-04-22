from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_tree(root: TreeNode) -> list:
    tree = []
    if root:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            tree.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return tree