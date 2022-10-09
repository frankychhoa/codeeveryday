# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.t=False
        def nodeDic(root,d):
            if root.val in d:
                d[root.val]+=1
            else:
                d[root.val]=1
            if root.left:
                nodeDic(root.left,d)
            if root.right:
                nodeDic(root.right,d)
        def checkTarget(root,d):
            if k-root.val in d:
                if k-root.val != root.val:
                    #t.append(True)
                    self.t=True
                elif d[k-root.val] > 1:
                    #t.append(True)
                    self.t=True
            if root.left:
                checkTarget(root.left,d)
            if root.right:
                checkTarget(root.right,d)
        d={}
        nodeDic(root,d)
        
        checkTarget(root,d)
        #if len(t)>0:
        if self.t==True:
            return True
        return False