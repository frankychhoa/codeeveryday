class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1 = 0
        ptr2 = len(s) -1
        
        while ptr1 != ptr2 and ptr1 < ptr2:
            head = s[ptr1]
            end = s[ptr2]
            s[ptr1] = end
            s[ptr2] = head
            ptr1 += 1
            ptr2 -= 1