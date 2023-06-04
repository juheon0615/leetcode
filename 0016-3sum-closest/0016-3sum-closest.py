class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = None
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if ret is None:
                    ret = s
                else:
                    curAbsDiff = abs(target - ret)
                    newAbsDiff = abs(target - s)
                    
                    if newAbsDiff < curAbsDiff:
                        ret = s
                        
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return s
        
        return ret