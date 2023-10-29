class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        

        
        
        visited = set()
        
        def dfs(cur, visited):
            visited.add(cur)
            for key in rooms[cur]:
                if key not in visited:
                    dfs(key, visited)
                
            
        
        dfs(0, visited)
        
        return True if len(visited) == len(rooms) else False
        