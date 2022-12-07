# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #count = 0
        def dfs(root,low,high):
            if root.val >= low and root.val <= high:
                self.count += root.val
            if root.val > low and root.left:
                dfs(root.left,low,high)
            if root.val < high and root.right:
                dfs(root.right,low,high)
        dfs(root,low,high)
        return self.count  