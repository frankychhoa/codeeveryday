class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict={}
        p_value=0
        for i in pattern:
            if i not in p_dict:
                p_value += 1
                p_dict[i]=p_value
        s_dict={}
        s_value=0
        word=""
        arr=[]
        for j,i in enumerate(s):
            if i == " " or j==len(s)-1:
                if j==len(s)-1:
                    word+=i
                arr.append(word)
                if word not in s_dict:
                    s_value+=1
                    s_dict[word]=s_value
                word=""
            else:
                word+=i
        print(arr)

        if len(arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            if p_dict[pattern[i]] != s_dict[arr[i]]:
                return False
        return True