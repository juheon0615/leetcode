class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def generate(left, right, path):
            if left == 0 and right == 0:
                ret.append(path)
                return
            
            if left > 0:
                generate(left-1, right, path + "(")
            
            if right > 0 and right > left:
                generate(left, right - 1, path + ")")
            
        generate(n,n,"")
        return ret
        
        