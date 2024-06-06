class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cnt = len(nums1) + len(nums2)

        def find_the_nth(nums1, nums2, nth):
            i1 = i2 = 0
            ret = []

            while len(ret) <= nth:
                if i1 == len(nums1):
                    # print(1)
                    ret.append(nums2[i2])
                    i2 += 1
                elif i2 == len(nums2):
                    # print(2)
                    ret.append(nums1[i1])
                    i1 += 1
                else:
                    if nums1[i1] < nums2[i2]:
                        # print(3)
                        ret.append(nums1[i1])
                        i1 += 1
                    else:
                        # print(4)
                        ret.append(nums2[i2])
                        i2 += 1
            # print(ret)
            return ret[-1]


        if cnt % 2 == 0:
            return (find_the_nth(nums1,nums2, cnt//2) + find_the_nth(nums1,nums2, cnt//2 - 1)) /2
        else:
            return find_the_nth(nums1,nums2,cnt//2)

            
        
        