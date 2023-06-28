class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        
        ret.append([1])
        
        for r in range(1, rowIndex + 1):
            rth = []
            for i in range(r + 1):
                if i == 0:
                    rth.append(1)
                elif i == r:
                    rth.append(1)
                else:
                    rth.append(ret[r - 1][i - 1] + ret[r - 1][i])
            
            ret.append(rth)
        
        return ret[rowIndex]