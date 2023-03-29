class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        prev = "."
        unknown = []
        ret = ""
        
        
        for d in dominoes:
            if d == ".":
                unknown.append(d)
            elif d == "L":
                if unknown:
                    if prev == "R":
                        ret += (len(unknown) // 2) * "R"
                        if len(unknown) % 2 == 1:
                            ret += "."
                        ret += (len(unknown) // 2) * "L"                            
                    else:
                        ret += len(unknown) * "L"
                    unknown.clear()
                ret += "L"
                prev = "L"
                
            elif d == "R":
                if unknown:
                    if prev == "R":
                        ret += len(unknown) * "R"
                    else:
                        ret += len(unknown) * "."
                        
                    unknown.clear()
                ret += "R"
                prev = "R"
        
        if prev == "R":
            ret += len(unknown) * "R"
        else:
            ret += len(unknown) * "."

        return ret
            
            
        
        