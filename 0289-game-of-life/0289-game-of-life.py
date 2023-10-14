class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        changes = []
        
        m = len(board)
        n = len(board[0])
        
        def findLiveCount(i,j):
            ret = 0
            off = [1,-1, 0]
            
            for oi in off:
                for oj in off:
                    if oi == 0 and oj == 0:
                        continue
                        
                    ii = i + oi
                    jj = j + oj
                    
                    if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 1:
                        ret += 1
            return ret
                        
        for i in range(m):
            for j in range(n):
                liveCount = findLiveCount(i,j)
                if liveCount < 2:
                    if board[i][j] != 0:
                        changes.append([i,j,0])
                elif liveCount > 3:
                    if board[i][j] == 1:
                        changes.append([i,j,0])
                elif liveCount == 3:
                    if board[i][j] == 0:
                        changes.append((i,j,1))
                else:
                    continue
        
        # print(changes)
        for change in changes:
            i,j,v = change
            board[i][j] = v
                
                
        