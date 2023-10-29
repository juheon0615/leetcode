class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        approach with bfs
        
        '''
        
        
        
        queue = [entrance]
        visited = set()
        visited.add((entrance[0], entrance[1]))
        steps = 0
        
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        M = len(maze)
        N = len(maze[0])
        
        escaped = False
        while queue:
            nextQueue = []
            for pos in queue:
                i,j = pos
                if (i == 0 or j == 0 or i == M - 1 or j == N - 1) and steps > 0:
                    escaped = True
                    break
                    
                for d in range(4):
                    ii = i + di[d]
                    jj = j + dj[d]
                    
                    if 0 <= ii < M and 0 <= jj < N and maze[ii][jj] == "." and (ii,jj) not in visited:
                        visited.add((ii,jj))
                        nextQueue.append([ii,jj])
            if escaped == True:
                break
                
            queue = nextQueue
            steps += 1

                        
        return -1 if escaped == False else steps
                