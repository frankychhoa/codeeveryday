class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        s=list(s)
        stack.append(s.pop(0))
        while s:
            if not stack:
                stack.append(s.pop(0))
            elif s[0] == stack[-1]:
                s.pop(0)
                stack.pop()
            else:
                stack.append(s.pop(0))
        return "".join(stack)


##stupid method
# s = list(s)
# index = 0
# while index < len(s)-1:
#     if len(s)==1:
#         break
#     if s[index] == s[index+1]:
#         del s[index]
#         del s[index]
#         index=0
        
#     else:
#         index +=1
# return "".join(s)