# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1=[]
        leaves2=[]
        def dfs(root,arr):
            if not root.left and not root.right:
                arr.append(root.val)
            if root.left:
                dfs(root.left,arr)
            if root.right:
                dfs(root.right,arr)
        dfs(root1,leaves1)
        dfs(root2,leaves2)
        
        if leaves1 == leaves2:
            return True
        return False