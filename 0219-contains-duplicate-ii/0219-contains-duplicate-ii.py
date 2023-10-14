class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mapNumIdx = {}
        ret = False
        for i in range(len(nums)):
            # print(mapNumIdx)
            if nums[i] not in mapNumIdx:
                mapNumIdx[nums[i]] = [i]
            else:
                for j in mapNumIdx[nums[i]]:
                    if abs(j-i) <= k:
                        ret = True
                        # print(i, " : ", j)
                        break
                mapNumIdx[nums[i]].append(i)
            
            if ret:
                break
        
        return ret
                        
            
        