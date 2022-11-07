class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num = list(num)
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        s = "".join(num)
        
        return int(s)