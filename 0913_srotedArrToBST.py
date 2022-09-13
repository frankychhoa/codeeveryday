# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(root,nums):
            print(nums)
            if len(nums) == 1:
                root.val = nums[0]
                return root
            elif len(nums) == 2:
                #print("make t")
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                return root
            else:
                root_val = nums[len(nums)//2]
                left = nums[:len(nums)//2]
                right = nums[len(nums)//2+1:]

                root.val = root_val
                if len(left) >0:
                    root.left = TreeNode()
                    root.left = tree(root.left, left)
                    #tree(root.left, left)
                if len(right) >0:
                    root.right = TreeNode()
                    root.right = tree(root.right,right)
                    #tree(root.right,right)
                return root
        if len(nums) == 0:
            return root
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        
        root = TreeNode()
        root.left = TreeNode()
        root.right = TreeNode()
        
        root_val = nums[len(nums)//2]
        root.val = root_val
        
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2+1:]
        l = tree(root.left,left)
        r = tree(root.right,right)
        
        root.left = l
        root.right = r
        return root