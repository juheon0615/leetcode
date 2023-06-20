class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(left, right, cur, ret):
            if left == 0 and right == 0:
                ret.append(cur)
            
            if left > 0:
                dfs(left -1, right, cur + "(", ret)
            
            if left < right and right > 0:
                dfs(left, right - 1, cur + ")", ret)
        
        
        ret = []
        
        dfs(n,n,"",ret)
        
        return ret
        
        