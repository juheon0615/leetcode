class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x1,x2,y1,y2):
            return math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))
        
        dists = []
        
        for point in points:
            dists.append([dist(0, point[0], 0, point[1]), point])
        
        dists.sort(key=lambda x:x[0])
        
        ret = []
        for i in range(k):
            ret.append(dists[i][1])
        
        return ret
            
        