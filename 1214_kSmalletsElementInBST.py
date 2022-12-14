# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #num=0
        def dfs(root):
            if not root.left and not root.right:
                self.num += 1
                if self.num == k:
                    return root.val
            else:
                if root.left:
                    x = dfs(root.left)
                    if x != None:
                        return x
                self.num += 1
                if self.num == k:
                    print("++")
                    return root.val
                if root.right:
                    x = dfs(root.right)
                    if x:
                        return x
        res = dfs(root)
        return res