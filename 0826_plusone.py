class Solution:
    def plusOne(self, digits) :
        
        index = len(digits)-1
        for i in range(len(digits)):
            if digits[index] < 9:
                digits[index] = digits[index]+1
                break
            else:
                digits[index] = 0
                if index == 0:
                    return [1]+digits
            index -=1
        return digits
                    