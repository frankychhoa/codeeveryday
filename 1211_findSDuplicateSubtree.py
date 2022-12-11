# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res=[]
        tree_d={}
        
        def dfs(root,path):
            
            if not root:
                return "#"
            path += ",".join([str(root.val),dfs(root.left,path),dfs(root.right,path)])
            
            if path not in tree_d:
                tree_d[path] = 1
            else:
                tree_d[path] += 1
            if tree_d[path] == 2:
                res.append(root)
            
            return path
        dfs(root,"")
        return res