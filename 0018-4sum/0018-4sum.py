class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        combs = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    comb = "%d %d %d %d" % (nums[i], nums[j], nums[l], nums[r])
                    
                    if s == target:
                        if comb not in combs:
                            ret.append([nums[i],  nums[j], nums[l], nums[r]])
                            combs.add(comb)
                        l += 1
                        r -+ 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        
        
        return ret
                    
                        
        