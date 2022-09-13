##need to be improved
class Solution:
    def isBalanced(self, root) -> bool:
        if root == None:
            return True
        result = []
        self.trace(result,root,0)
        if False in result:
            return False
        return True
    
    def trace(self, result, root, count):
        left = count
        right = count
        if root.left == None and root.right == None:
            return count
        if root.left != None:
            left = self.trace(result, root.left, count+1)
            
        if root.right != None:
            right = self.trace(result, root.right, count+1)
        print(left)
        print(right)
        if abs(left-right) > 1:
            result.append(False)
        if left >= right:
            return left
        else:
            return right