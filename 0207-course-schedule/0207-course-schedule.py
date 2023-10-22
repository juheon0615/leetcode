class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        pr = {}        
        for prerequisite in prerequisites:
            src, dst = prerequisite
            
            if dst not in pr:
                pr[dst] = []
            
            pr[dst].append(src)
        
        visited = set()
        updated = True
        while updated:
            updated = False
            for i in range(numCourses):
                if i in visited:
                    continue
                
                if i in pr and len(pr[i]) > 0:
                    canTake = True
                    for j in pr[i]:
                        if j not in visited:
                            canTake = False
                            break
                    if canTake:
                        visited.add(i)
                        updated = True
                else:
                    visited.add(i)
                    updated = True
        return True if len(visited) >= numCourses else False
                
                
            
            
        
        