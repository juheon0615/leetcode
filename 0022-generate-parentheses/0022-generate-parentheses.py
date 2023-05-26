class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def branch(left, right, cur, ret):
            if left == 0 and right == 0:
                ret.append(cur)
            
            if left > 0:
                branch(left -1, right, cur + "(", ret)
            
            if left < right and right > 0:
                branch(left, right - 1, cur + ")", ret)
        
        
        ret = []
        
        branch(n,n,"",ret)
        
        return ret
        
        