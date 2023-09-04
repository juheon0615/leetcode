class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] != 0:
            return -1
        #bfs
        q = [(0,0)]
        visited = set()
        visited.add((0,0))
        
        
        ret = 1
        n = len(grid)
        reached = False
        
        directions = [[0,1], [1,0], [0,-1], [-1,0], [1,-1], [-1,1], [-1,-1], [1,1]]
        
        while q:
            nextQ = []
            # print(q)
            while q:
                i, j = q.pop(0)
                
                if i == n - 1 and j == n - 1:
                    reached = True
                    break
                
                for d in directions:
                    di = i + d[0]
                    dj = j + d[1]
                    
                    if di >= 0 and di < n and dj >=0 and dj < n and grid[di][dj] == 0 and (di,dj) not in visited:
                        nextQ.append((di,dj))
                        visited.add((di,dj))
            
            if reached:
                break
            
            ret += 1
            q = nextQ
            
        
        return ret if reached else -1
        
        
        