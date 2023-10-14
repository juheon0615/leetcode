class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        
        1, 3, 0, 0, 4, 0, 2
        
        1,3 => 1
        1,4 => 4
        3,4 => 9
        3,2 => 10
        4,2 => 4
        
        4,2 does not need to be considered. 
        because 3,2 is the biggest area that can be formed with 2 on the right. 
        area is formed with the min value
        '''
        
        
        i = 0 
        j = len(height) - 1
        ret = 0
        while i < j:
            area = min(height[i],height[j]) * (j - i)
            ret = max(ret,area)
            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return ret
            
        
        
        