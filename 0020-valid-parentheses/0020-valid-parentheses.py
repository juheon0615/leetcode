class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        ret = True
        for p in s:
            if p == "(" or p == "{" or p == "[":
                opens.append(p)
            else:
                if len(opens) == 0:
                    ret = False
                    break
                
                if p == ")":
                    if opens.pop(-1) != "(":
                        ret = False
                        break
                elif p == "}":
                    if opens.pop(-1) != "{":
                        ret = False
                        break
                else:
                    if opens.pop(-1) != "[":
                        ret = False
                        break     
        
        if len(opens) != 0:
            ret = False
            
        return ret