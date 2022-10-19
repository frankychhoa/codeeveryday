class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up=list(string.ascii_uppercase)
        low=list(string.ascii_lowercase)
        if word[-1] in up:
            for i in word:
                if i not in up:
                    return False
        if word[-1] in low:
            for i in range(1,len(word)):
                if word[i] not in low:
                    return False
        return True