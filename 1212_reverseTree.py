# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return root
            if not root.left and not root.right:
                return root
            if root.left:
                root.left = dfs(root.left)
            if root.right:
                root.right = dfs(root.right)
            l,r = root.left, root.right
            root.left = r
            root.right = l
            return root
        return dfs(root)