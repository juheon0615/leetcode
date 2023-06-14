class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ret = True
        sqChecks = [set() for _ in range(3)]
        rCheck = set()
        cChecks = [set() for _ in range(9)]
        for i, row in enumerate(board):
            rCheck.clear()
            
            if i % 3 == 0:
                for sqCheck in sqChecks:
                    sqCheck.clear()
                
            for j, num in enumerate(row):
                if num == ".":
                    continue
                cCheck = cChecks[j]
                if num in cCheck:
                    ret = False
                    break
                else:
                    cCheck.add(num)
                    
                sqCheck = sqChecks[j//3]
                
                if num in sqCheck:
                    ret = False
                    break
                else:
                    sqCheck.add(num)
                
                
                if num in rCheck:
                    ret = False
                    break
                else:
                    rCheck.add(num)
            
            if ret == False:
                break
        
        return ret
                
        