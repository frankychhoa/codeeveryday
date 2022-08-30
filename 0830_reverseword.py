class Solution:
    def reverseWords(self, s: str) -> str:
        ptr1 = 0
        ptr2 = 0
        arr = []
        while ptr2 < len(s):
            print(ptr2)
            if s[ptr1] == " " and s[ptr2] == " ":
                ptr1 += 1
                ptr2 += 1
            elif s[ptr2] != " " and ptr2 != len(s)-1:
                ptr2 += 1
            elif ptr2 >= ptr1:
                if s[ptr2] == " ":
                    arr.append(s[ptr1:ptr2])
                    ptr1 = ptr2
                elif ptr2 == len(s)-1:
                    arr.append(s[ptr1:])
                    ptr2 += 1
                    
        result = ""
        for i in range(len(arr)):
            result += arr[len(arr)-i-1] 
            if (len(arr)-i-1) > 0:
                result += " "
        return result