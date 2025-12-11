class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = {}
        ret = 0
        left = 0

        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]] = 0
            counts[s[i]] += 1

            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            
            ret = max(ret, i - left + 1)
        return ret 

        