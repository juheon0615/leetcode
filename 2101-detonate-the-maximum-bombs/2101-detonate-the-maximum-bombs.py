class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def isAdj(bomb1, bomb2):
            
            x1 = bomb1[0]
            y1 = bomb1[1]
            r1 = bomb1[2]
            
            x2 = bomb2[0]
            y2 = bomb2[1]
            r2 = bomb2[2]
            
            d = math.sqrt(pow((y2-y1),2) + pow((x2-x1),2))
            
            return True if d <= r1 else False
        
        

        ret = 0
        for i in range(len(bombs)):
            print("for ", i)
            
            def dfs(bomb):
                d = 1
                for k in range(len(bombs)):
                    if k not in visited and isAdj(bomb, bombs[k]):
                        visited.add(k)
                        d += dfs(bombs[k])
                return d
            
            visited = set()
            visited.add(i)
            ret = max(ret, dfs(bombs[i]))
            print(ret, " : " ,visited)
        
        return ret
                        
            
            
            
        