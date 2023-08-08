class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        
        while a > 0 or b > 0 or c > 0:
            
            aa = a & 1
            bb = b & 1
            cc = c & 1
            
            if cc == 0:
                ret += (aa + bb)
            else:
                if aa | bb:
                    pass
                else:
                    ret += 1
            
            # print("aa %d bb %d cc %d ret %d" %(aa,bb,cc,ret))
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return ret
            
            
            
            
            
        