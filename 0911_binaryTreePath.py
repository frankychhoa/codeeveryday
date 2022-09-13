# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root) :
        result = []
        s = ""
        self.path(root, result, s)
        return result
    def path(self, root, nums,s):
        s += str(root.val)
        if root.left == None and root.right == None:
            nums.append(s)
            print(nums)
        if root.left != None:
            sl = s+"->"
            self.path(root.left, nums, sl)
        if root.right != None:
            sr = s+"->"
            self.path(root.right, nums, sr)