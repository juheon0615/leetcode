class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]


        dp[0] = True

        wordSet = set(wordDict)
        wordLengths = set(len(word) for word in wordDict)

        for i in range(1, len(s) + 1):
            for l in wordLengths:
                j = i - l
                if j >= 0 and dp[j] and s[j:j + l] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]
        

        