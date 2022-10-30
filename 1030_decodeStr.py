class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            substr=""
            k=""
            if i != "]":
                stack.append(i)
            else:
                while stack[-1] != "[":
                    s = stack.pop()
                    substr = s+substr
                stack.pop()
                
                while stack and stack[-1].isdigit():

                    n = stack.pop()
                    k = n+k
                stack.append(int(k)*substr)
        res = ""
        for i in stack:
            res += i
        return res