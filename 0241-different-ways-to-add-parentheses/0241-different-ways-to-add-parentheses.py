class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        
        def dfs(exp):
            if exp in mem:
                return mem[exp]
               
            if "+" not in exp and "-" not in exp and "*" not in exp:
                return [int(exp)]
            
            ret = []
            for i,e in enumerate(exp):
                
                if e in "+-*":
                    lhs = dfs(exp[0:i])
                    rhs = dfs(exp[i+1:])
                    
                    for l in lhs:
                        for r in rhs:
                            if e == "+":
                                ret.append(l + r)
                            elif e == "-":
                                ret.append(l - r)
                            else:
                                ret.append(l * r)
            
            mem[exp] = ret
            return mem[exp]
        mem = {}
        return dfs(expression)