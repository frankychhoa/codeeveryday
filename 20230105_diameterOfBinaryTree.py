# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.m=0
        def dfs(root,count):
            if not root:
                return count-1
            left = dfs(root.left,count+1)
            right = dfs(root.right,count+1)
            print(left)
            print(right)
            if left + right - count*2 > self.m:
                self.m = left+right - count*2
            return max(left,right)

        
        if not root:
            return 0
        dfs(root,0)
        return self.m