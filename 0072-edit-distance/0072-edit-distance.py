class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]

        
        
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
        return dp[len(word1)][len(word2)]
        
#         mem = [[-1 for _ in range(len(word2))] for __ in range(len(word1))]
        
#         def match(i, j):
#             # print("i: %d %s : j: %d %s" %(i, word1[:i], j, word2[:j]))
#             if i == len(word1):
#                 return len(word2) - j
            
#             if j == len(word2):
#                 return len(word1) - i
        
#             if mem[i][j] != -1:
#                 return mem[i][j]
            
#             if word1[i] == word2[j]:
#                 return match(i+1, j+1)
            
            
#             ret = match(i+1, j)
#             ret = min(ret, match(i,j + 1))
#             ret = min(ret, match(i + 1, j + 1))
            
#             mem[i][j] = ret + 1
            
#             return mem[i][j]

#         return match(0,0)
            