# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            if root.left:
                ##if leaf node
                if not root.left.left and not root.left.right and root.left.val == target:
                    root.left = None
                else:
                    dfs(root.left)
            if root.right:
                if not root.right.left and not root.right.right and root.right.val == target:
                    root.right = None
                else:
                    dfs(root.right)
            if root.left:
                ##if leaf node
                if not root.left.left and not root.left.right and root.left.val == target:
                    root.left = None 
            if root.right:
                if not root.right.left and not root.right.right and root.right.val == target:
                    root.right = None
        dfs(root)
        if root.val == target and not root.left and not root.right:
            return None
        return root