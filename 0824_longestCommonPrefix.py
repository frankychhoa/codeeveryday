class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        commonStr = self.findCommon(strs[0],strs[1])
        for i in range(2,len(strs)):
            commonStr = self.findCommon(commonStr,strs[i])
        return commonStr
            
    def findCommon(self,str1,str2):
        common = ""
        index = 0
        while index < len(str1) and index < len(str2):
            if str1[index] == str2[index]:
                common += str1[index]
                index += 1
            else: 
                break
        return common