class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        s = []
        
        for t in tokens:
            if t in ops:
                rhs = s.pop(-1)
                lhs = s.pop(-1)
                res = 0
                if t == "+":
                    res = lhs + rhs
                elif t == "-":
                    res = lhs - rhs
                elif t == "*":
                    res = lhs * rhs
                else:
                    res = int(lhs / rhs)
                
                s.append(res)
                # print("%d %s %d" % (lhs, t, rhs))
            else:
                s.append(int(t))
            # print(s)
        return s[0]
        
        