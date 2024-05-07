class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        queue = [0]
        visited = set()
        
        
        while queue:
            nextQ = []
            
            for cur in queue:
                if cur == len(s):
                    return True
                for word in wordDict:
                    end = len(word) + cur
                    # print("%d %d %s" %(cur,end,word))
                    if end <= len(s) and s[cur:end] == word and end not in visited:
                        visited.add(end)
                        nextQ.append(end)
                # print(nextQ)
            queue = nextQ
                

        return False