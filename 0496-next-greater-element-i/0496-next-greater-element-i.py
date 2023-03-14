class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {x: -1 for x in nums1}
        s = []
        
        for num in nums2:
            while s and s[-1] < num:
                prev = s.pop(-1)
                if prev in d: 
                    d[prev] = num
            s.append(num)
            
        
        return [d[x] for x in nums1]
        
        