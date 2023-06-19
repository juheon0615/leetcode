class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        end = n * n
        visited = [False for _ in range(n * n)]

        def sqToCoordinate(sq):
            d = (sq - 1) // n
            r = (sq - 1) % n
            i = 0
            j = 0
            
            if d % 2 == 0:
                i = n - d - 1
                j = r
            else:
                i = n - d - 1
                j = n - r - 1
                
            return i,j
        
        q = [1]
        ret = -1
        cnt = -1
        while q:
            nextQ = []
            cnt += 1
            # print(q)
            while q:
                sq = q.pop(0)
                
                if sq == end:
                    q.clear()
                    nextQ.clear()
                    ret = cnt
                    break
                    
                if visited[sq]:
                    continue
                
                
                
                for d in range(6,0,-1):
                    newSq = sq + d
                    if newSq > end:
                        continue
                    i, j = sqToCoordinate(newSq)
                    if board[i][j] != -1:
                        newSq = board[i][j]
                    
                    nextQ.append(newSq)
                        
                visited[sq] = True
            q = nextQ
        return ret