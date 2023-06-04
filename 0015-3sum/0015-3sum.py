class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # on brute force i,j,k O(n^3)
        # sort then 2 cursor, O(nlogn) + O(n^2)
        
        ret = []
        retSet = set()
        
        nums.sort()
        prevNum = None
        for i in range(0, len(nums) - 2):
            if nums[i] == prevNum:
                continue
            
            j = i+1
            k = len(nums) - 1
            
            while j < k:                
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    key = "%d %d %d" % (nums[i], nums[j], nums[k])
                    if key not in retSet:
                        ret.append([nums[i], nums[j], nums[k]])
                        retSet.add(key)
                    k -= 1
                    j += 1
            
            prevNum = nums[i]
        
        return ret
            