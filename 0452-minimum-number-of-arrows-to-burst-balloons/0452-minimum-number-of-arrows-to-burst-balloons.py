class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        merged = []
        points.sort(key=lambda x:x[0])
        
        curLeft = points[0][0]
        curRight = points[0][1]
        
        for i in range(1, len(points)):
            x1 = points[i][0]
            x2 = points[i][1]
            
            
            if curLeft <= x1 <= curRight:
                curLeft = max(curLeft,x1)
                curRight = min(curRight,x2)
            else:
                merged.append([curLeft, curRight])
                curLeft = x1
                curRight = x2
        merged.append([curLeft, curRight])
        print(merged)
        return len(merged)
        