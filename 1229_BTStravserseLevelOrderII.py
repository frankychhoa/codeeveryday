# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        d={}
        res=[]
        def dfs(root,count):
            if count not in d:
                d[count]=[root.val]
            else:
                d[count]+=[root.val]
            
            if root.left:
                dfs(root.left,count+1)
            if root.right:
                dfs(root.right,count+1)

        dfs(root,0)
        for i in range(len(d)-1,-1,-1):
            res.append(d[i])
        return res