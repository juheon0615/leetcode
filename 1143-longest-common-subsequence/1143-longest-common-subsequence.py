class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         t = [[0 for t2 in range(len(text2) + 1)] for t1 in range(len(text1) + 1) ]
        
#         for i in range(1, len(text1) + 1):
#             for j in range(1, len(text2) + 1):
#                 if text1[i-1] == text2[j-1]:
#                     t[i][j] = t[i-1][j-1] + 1
#                 else:
#                     t[i][j] = max(t[i-1][j], t[i][j-1])
        
#         return t[len(text1)][len(text2)]
    
        
        mem = [[-1 for t2 in range(len(text2))] for t1 in range(len(text1))]
        
        def lcs(text1, text2, t1, t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            if mem[t1][t2] != -1:
                return mem[t1][t2]
            
            ret = 0
            
            if text1[t1] == text2[t2]:
                ret = lcs(text1, text2, t1 + 1, t2 + 1) + 1
            else:
                ret = max(lcs(text1, text2, t1 + 1, t2), lcs(text1, text2, t1, t2 + 1))
            
            mem[t1][t2] = ret
            
            return ret
        
        answer = lcs(text1, text2, 0, 0)
        # print(mem)
        return answer
         
    
    '''
    memoization version
    '''
#         mem = {}
        
#         def lcs(text1, text2, i1, i2):
#             if i1 == -1 or i2 == -1:
#                 return 0
            
#             if i1 in mem and i2 in mem[i1]:
#                 return mem[i1][i2]
            
#             ret = 0
#             if text1[i1] == text2[i2]:
#                 ret = 1 + lcs(text1,text2, i1 - 1, i2 - 1)
            
            
#             else:
#                 ret = max(lcs(text1, text2, i1 - 1, i2), lcs(text1, text2, i1, i2 - 1))
            
#             if i1 not in mem:
#                 mem[i1] = {}
            
#             mem[i1][i2] = ret
            
#             return ret
        
#         mem = {}
#         return lcs(text1, text2, len(text1) - 1, len(text2) - 1)
            
            
        