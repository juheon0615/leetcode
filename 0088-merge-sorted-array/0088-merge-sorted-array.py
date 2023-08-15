class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        
        ret = []
        
        while i < m or j <n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    ret.append(nums1[i])
                    i += 1
                else:
                    ret.append(nums2[j])
                    j += 1
            elif i < m:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        
        
        for i in range(len(ret)):
            nums1[i] = ret[i]
                
                
        