class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack2=[]
        stack3=[]
        for i in s:
            if i == "(" or i =="[" or i=="{":
                stack+=[i]
            
            elif i == ")":
                if len(stack)==0 or stack[-1] != "(":
                    return False
                else: stack.pop()
            elif i == "]" :
                if len(stack)==0 or stack[-1] != "[":
                    print(stack)
                    return False
                else: stack.pop()
            elif i == "}" :
                if len(stack)==0 or stack[-1] != "{":
                    print(stack)
                    return False
                else: stack.pop()
        if len(stack)!=0:
            return False
        

        return True