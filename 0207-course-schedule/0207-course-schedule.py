class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        '''
        make dict of edges
        make dict of pre req counts for each class
        make visited set
        bfs on classes
        '''
        
        edges = {}
        reqCounts = {}
        
        
        for prerequisite in prerequisites:
            a = prerequisite[0]
            b = prerequisite[1]
            
            if a not in edges:
                edges[a] = []
            
            if b not in edges[a]:
                edges[a].append(b)
            
            if a not in reqCounts:
                reqCounts[a] = 0
            
            if b not in reqCounts:
                reqCounts[b] = 0
            reqCounts[b] += 1
            
        
        # print(edges)
        # print(reqCounts)
        
        q = []
        visited = set()

        for rc in reqCounts:
            if reqCounts[rc] == 0:
                q.append(rc)
                visited.add(rc)
        
        while q:
            nextQ = []
            for a in q:
                for b in edges[a]:
                    if reqCounts[b] > 0:
                        reqCounts[b] -= 1
                    if reqCounts[b] == 0 and b not in visited and b in edges:
                        visited.add(b)
                        nextQ.append(b)
            q = nextQ
        
        ret = True
        
        for req in reqCounts:
            if reqCounts[req] > 0:
                ret = False
        return ret
            
            