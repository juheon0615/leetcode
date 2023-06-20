class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruscal
        
        
        edges = [] # edge: [src, dst, dist]
        parent = [i for i in range(len(points))]
        rank = [0 for _ in range(len(points))]
        
        def getParent(parent, i):
            if parent[i] == i:
                return i
            else:
                return getParent(parent, parent[i])
            
        def union(parent, rank, x, y):
            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                rank[x] += 1
            

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) 
                
                edge = [i, j, dist]
                edges.append(edge)
        
        
        edges.sort(key=lambda x: x[2])
        
        cost = 0
        e = 0
        for edge in edges:
            src = edge[0]
            dst = edge[1]
            dist = edge[2]
            
            pSrc = getParent(parent, src)
            pDst = getParent(parent, dst)
            
            if pSrc != pDst:
                cost += dist
                e += 1
                union(parent, rank, pSrc, pDst)

                
            if e == len(points) - 1:
                break
        
        return cost
            
        