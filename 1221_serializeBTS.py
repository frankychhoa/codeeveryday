# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.s=""
        self.arr=[]
        self.t=TreeNode()

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        self.arr.append(str(root.val))
        while queue:
            #print(self.arr)
            element = queue.pop(0)
            try:
                self.arr.append(str(element.left.val))
                queue.append(element.left)
            except:
                self.arr.append("null")
            try:
                self.arr.append(str(element.right.val))
                queue.append(element.right)
            except:
                self.arr.append("null")
        print(",".join(self.arr))
        return ",".join(self.arr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data+=","
        v=""
        for i in data:
            if i == ",":
                self.arr.append(v)
                v=""
            else:
                v+=i
        self.t = TreeNode(int(self.arr.pop(0)))
        queue=[self.t]
        while len(self.arr) > 0:
            #print(self.arr)
            if len(queue) == 0:
                break
            element = queue.pop(0)
            nextVal = self.arr.pop(0)
            if nextVal != "null":
                element.left = TreeNode(int(nextVal))
                queue.append(element.left)

            try:
                nextVal = self.arr.pop(0)
                if nextVal != "null":
                    element.right = TreeNode(int(nextVal))
                    queue.append(element.right)
            except:
                pass
        return self.t    
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))