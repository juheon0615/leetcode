class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        if len(s) == 0:
            return True

        for i in range(len(t)):
            if t[i] == s[si]:
                si += 1
                if si >= len(s):
                    return True
        return False
        