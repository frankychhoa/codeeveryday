# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,total):
            if not root:
                return False
            if total + root.val == targetSum and not root.left and not root.right:
                return True
            left = dfs(root.left,total+root.val)
            right = dfs(root.right,total+root.val)

            if left == True or right == True:
                return True
            return False
        
        res = dfs(root,0)
        return res