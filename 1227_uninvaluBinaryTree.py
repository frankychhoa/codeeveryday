# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        target = root.val
        def dfs(root):
            if not root:
                return True
            if root.val != target:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            if not left or not right:
                return False
            return True
        res = dfs(root)
        return res