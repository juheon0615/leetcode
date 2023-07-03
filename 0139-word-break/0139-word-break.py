class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dp(cur, words, mem):
            if cur in mem:
                return mem[cur]
            
            if cur == "":
                return True
            
            ret = False
            for word in words:
                if len(cur) >= len(word) and cur[:len(word)] == word:
                    ret = ret or dp(cur[len(word):], words, mem)
            
            mem[cur] = ret
            
            return mem[cur]
        
        mem = {}
        
        return dp(s, wordDict, mem)
    