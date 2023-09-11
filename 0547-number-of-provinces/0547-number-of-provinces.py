class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        ret = 0
        connected = {}
    
        for i in range(n):
            connected[i] = []
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    connected[i].append(j)
                    
        
        visited = set()
        for i in range(n):
            if i in visited:
                continue
                
            #bfs
            q = [i]
            
            while q:
                nextQ = []
                while q:
                    j = q.pop(0)
                    
                    for k in connected[j]:
                        if k not in visited:
                            visited.add(k)
                            nextQ.append(k)
                q = nextQ
            
            ret += 1
        
        return ret
                    
                    
            
                
            
            
        
        
                
                
                
            
        
        