class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        ps = None
        ret = True
        
        for i in range(1, len(coordinates)):
            s = None
            if coordinates[i-1][0] == coordinates[i][0]:
                pass
            else:
                s = (coordinates[i][1] - coordinates[i-1][1]) // (coordinates[i][0] - coordinates[i-1][0])
            
            if i == 1:
                ps = s
            else:
                if s != ps:
                    ret = False
                    break
        
        return ret
            
        