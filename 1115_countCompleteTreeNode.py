# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if not root.left and not root.right:
            return 1
        left=0
        right=0
        try:
            left = self.countNodes(root.left)
        except:
            left = 0
        try:
            right = self.countNodes(root.right)
        except:
            right = 0
        return 1+left+right