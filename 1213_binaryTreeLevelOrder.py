# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return self.res
        d={}
        def dfs(root,num):
            if num not in d:
                d[num] = [root.val]
            else:
                d[num] += [root.val]
            if root.left:
                dfs(root.left,num+1)
            if root.right:
                dfs(root.right,num+1)
        dfs(root,0)
        for i in range(len(d)):
            self.res.append(d[i])
        return self.res