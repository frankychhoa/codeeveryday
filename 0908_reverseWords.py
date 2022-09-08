class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        result = ""
        for i in s:
            
            if i != " ":
                word = i + word
            else:
                
                result += word
                result += " "
                word = ""
        result += word
        return result