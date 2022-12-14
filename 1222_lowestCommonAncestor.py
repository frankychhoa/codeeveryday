# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = TreeNode(0)
        self.candidate = TreeNode(0)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #res = TreeNode(0)
        arr = [p.val,q.val]
        self.res = TreeNode(root.val)
        def dfs(root,can):
            # if not root:
            #     pass
            if root.val == p.val or root.val == q.val:
                if can.val >= 10**10:
                    can = root
            if root.left:
                if root.left.val == p.val or root.left.val == q.val:
                    if root.right and (root.right.val == p.val or root.right.val == q.val):
                        self.res = root
                        return True
                    
                    elif can.val < 10**10:
                        self.res = can

                    elif can.val >= 10**10:
                        dfs(root.left,root.left)
                else:
                    if root.right and (root.right.val == p.val or root.right.val == q.val):
                        dfs(root.left,root)
                    else:
                        dfs(root.left,can)
            if root.right:
                if root.right.val == p.val or root.right.val == q.val:
                    if can.val < 10**10:
                        self.res = can
                    elif can.val >= 10**10:
                        dfs(root.right,root.right)
                else:
                    if root.left and (root.left.val == p.val or root.left.val == q.val):
                        dfs(root.right,root)
                    else:
                        dfs(root.right,can)
        
        dfs(root,TreeNode(10**10))
        return self.res

class Solution:
    def __init__(self):
        self.res = TreeNode(0)
        self.arr=[]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #res = TreeNode(0)
        if not root:
            return None
        def dfs(root,a):
            if root.val == p.val or root.val == q.val:
                x = root.val
                self.arr.append(a)
            if root.left:
                x = root.left.val
                dfs(root.left,a+[root.left])
            if root.right:
                x = root.right.val
                dfs(root.right,a+[root.right])
        dfs(root,[root])
        a,b = self.arr[0],self.arr[1]
        a_set = set()
        b_list = []
        b_dic = {}
        for i in range(len(a)):
            a_set.add(a[i].val)
        for i in range(len(b)):
            b_list.append(b[i].val)
            b_dic[b[i].val] = b[i]
        b_list.reverse()
        for i in b_list:
            if i in a_set:
                return b_dic[i]