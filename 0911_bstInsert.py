# class KthLargest:

#     def __init__(self, k: int, nums):
#         self.k = k
#         self.root = TreeNode(100000)
#         if len(nums) > 0:
#             self.root = TreeNode(nums[0])
#             for i in range(1,len(nums)):
#                 self.root.insert(self.root,nums[i])
        


#     def add(self, val: int) -> int:
#         if self.root.val == 100000:
#             self.root.val = val
#         self.root.insert(self.root, val)
#         arr = []
#         self.inorder(self.root, arr)
#         self.nums = arr
#         index = self.k * -1
#         if len(arr) < self.k:
#             return -1

#         return arr[index]
        
    
#     def inorder(self, root, nums):
#         if root.left != None:
#             self.inorder(root.left, nums)
#         nums.append(root.val)
#         if root.right != None:
#             self.inorder(root.right, nums)



        

        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, root, val):
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insert(root.right, val)
        elif val <= root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, root, val):
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insert(root.right, val)
        elif val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)