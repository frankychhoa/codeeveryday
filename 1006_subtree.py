# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def findHead(root, val,arr,subRoot,t):
            if root.val == val:
                count = checkSame(root,subRoot,[])
                if len(count) == 0:
                    t.append(True)
            if root.left != None:
                findHead(root.left,val,[],subRoot,t)
            if root.right != None:
                findHead(root.right,val,[],subRoot,t)
        def checkSame(r1,r2,arr):

            if r1.val != r2.val:
                arr.append(False)
            
            if r1.left != None and r2.left != None:
                checkSame(r1.left,r2.left,arr)
            elif r1.left != None or r2.left!=None:
                arr.append(False)
            if r1.right!=None and r2.right!=None:
                checkSame(r1.right,r2.right,arr)
            elif r1.right != None or r2.right!=None: 
                arr.append(False)
            return arr
        def checkSingle(root,val,t):
            if root.left == None and root.right==None:
                print(root.val)
            if root.left == None and root.right==None and root.val ==val:
                t.append(True)
            if root.left!=None:
                checkSingle(root.left,val,t)
            if root.right!=None:
                checkSingle(root.right,val,t)
        
        
        
        if subRoot.left == None and subRoot.right == None:
            res=[]
            checkSingle(root,subRoot.val,res)
            if res:
                return True
            else:
                return False
        res=[]
        t=[]
        findHead(root,subRoot.val,res,subRoot,t)
        if len(t)>0:
            return True
        else:
            return False
        

        

    
            
            