# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
       
        
        def find(root, arr):
            if root.left:
                find(root.left,arr)
            arr.append(root.val)
            if root.right:
                find(root.right,arr)
            
        arr = []
        find(root,arr)
        arr.sort()
        m = 100000
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < m:
                m = arr[i+1] - arr[i]
        return m