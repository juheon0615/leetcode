class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        last = 0
        ret = 0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= last:
                last = seen[s[i]] + 1

            seen[s[i]] = i
            # print("i %d last %d " % (i, last))
            # print(seen)
            ret = max(ret, i - last + 1)
        return ret



        