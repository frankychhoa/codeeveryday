class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=""
        alphabet = set(list(string.ascii_lowercase) + list(string.ascii_uppercase))
        num = [str(i) for i in range(10)]
        num = set(num)
        for i in s:
            if i in alphabet:
                check+=(str.lower(i))
            elif i in num:
                check+=i
        ptr1, ptr2 = 0, len(check)-1
        if not check:
            return True

        while ptr1 != ptr2 and ptr1 < ptr2:
            if check[ptr1] != check[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True