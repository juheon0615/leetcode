class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def dfs(cur1, cur2, cur3, mem):
            
            if cur1 == len(s1) and cur2 == len(s2) and cur3 == len(s3):
                return 1
            
            if cur3 == len(s3):
                return 0
            
            # print("cur1: ", cur1, " cur2: ", cur2, " cur3: ", cur3)

            if cur1 in mem and cur2 in mem[cur1]:
                return mem[cur1][cur2]
            

            ret = 0
            if cur1 < len(s1):
                if s1[cur1] == s3[cur3]:
                    ret += dfs(cur1+1, cur2, cur3+1, mem)
            
            if cur2 < len(s2):
                if s2[cur2] == s3[cur3]:
                    ret += dfs(cur1, cur2 + 1, cur3 + 1, mem)
            
            if cur1 not in mem:
                mem[cur1] = {}
            mem[cur1][cur2] = ret
            
            return mem[cur1][cur2]
        
        mem = {}
        

        
        return True if dfs(0,0,0,mem) > 0 else False
            
        