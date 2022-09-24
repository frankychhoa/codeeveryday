class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def addToArr(root, target, arr, result):
            if sum(arr+[root.val]) == target and root.left == None and root.right == None:
                result.append(arr+[root.val])
                
            if root.left != None:
                addToArr(root.left, target, arr+[root.val], result)
            if root.right != None:
                addToArr(root.right, target, arr+[root.val], result)
        if root == None:
            return []
        result = []
        addToArr(root, targetSum, [], result)
        return result