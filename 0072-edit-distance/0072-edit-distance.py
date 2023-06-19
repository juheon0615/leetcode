class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = [[-1 for _ in range(len(word2))] for __ in range(len(word1))]
        
        def match(i, j):
            # print("i: %d %s : j: %d %s" %(i, word1[:i], j, word2[:j]))
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
        
            if mem[i][j] != -1:
                return mem[i][j]
            
            if word1[i] == word2[j]:
                return match(i+1, j+1)
            
            
            ret = match(i+1, j)
            ret = min(ret, match(i,j + 1))
            ret = min(ret, match(i + 1, j + 1))
            
            mem[i][j] = ret + 1
            
            return mem[i][j]
        
        ret = match(0,0)
        return ret
            