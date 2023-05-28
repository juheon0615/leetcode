class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalCnt = len(nums1) + len(nums2)
        
        i1 = i2 = 0
        merged = []
        
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 == len(nums1):
                merged.append(nums2[i2])
                i2 += 1
            elif i2 == len(nums2):
                merged.append(nums1[i1])
                i1 += 1
            else:
                if nums1[i1] < nums2[i2]:
                    merged.append(nums1[i1])
                    i1 += 1
                else:
                    merged.append(nums2[i2])
                    i2 += 1
        
        print(merged)
        
        ret = 0.0
        
        if len(merged) % 2 == 0:
            ret = (merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2
        else:
            ret = merged[len(merged) // 2] * 1.0
        
        return ret

        