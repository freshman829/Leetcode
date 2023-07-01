class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        step1 = 0
        step2 = 0
        if len(s) == 0:
            return True
        while step2 < len(t):
            if s[step1] == t[step2]:
                step1 += 1
                if step1 == len(s):
                    return True
            step2 += 1
        if step1 == len(s):
            return True
        return False