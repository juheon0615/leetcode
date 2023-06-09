class Solution:
    def checkValidString(self, s: str) -> bool:
        h = l = 0
        
        for c in s:
            if c == "(":
                h += 1
                l += 1
            elif c == ")":
                h -= 1
                l = max(l-1,0) # cant reduce if 0
            else:
                h += 1
                l = max(l-1,0)
            
            if h < 0:
                return False
        
        return True if l == 0 else False
            
        

        
        