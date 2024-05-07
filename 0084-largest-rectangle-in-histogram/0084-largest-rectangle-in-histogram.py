class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        ret = 0
        for i, h in enumerate(heights):
            while stack and stack[-1][1] >= h:
                ii, hh = stack.pop()
                
                w = 0
                if not stack:
                    w = i
                else:
                    w = i - stack[-1][0] -1
                ret = max(ret, w * hh )
            stack.append((i,h))
        
        while stack:
            i, h = stack.pop()
            w = 0
            if not stack:
                w = len(heights)
            else:
                w = len(heights) - stack[-1][0] -1
            ret = max(ret, w * h)
        
        return ret
            
            
        