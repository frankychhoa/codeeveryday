class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # if goal[0] not in s:
        #     return False
        for i in range(len(s)):
            if s[i] == goal[0]:
                diff = False
                for m,n in zip(s[i:]+s[:i],goal):
                    if m != n:
                        diff = True
                        break
                if diff is False:
                    return True
        return False