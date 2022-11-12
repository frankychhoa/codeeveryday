# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root,lower,upper):
            if root.left:
                if root.left.val >= root.val or root.left.val <= lower:
                    return False
            if root.right:
                if root.right.val <= root.val or root.right.val >= upper:
                    return False
            left = True
            right=True
            try:
                left =  valid(root.left,lower,root.val)
            except:
                left = True
            try:
                right = valid(root.right,root.val,upper)
            except:
                right = True
            if left == right == True:
                return True
            return False

        return valid(root,-2**32,2**32)