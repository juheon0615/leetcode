class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ret = None
        acc = 0
        
        for i, num in enumerate(nums):
            acc += num
            # print("add i: %d num: %d acc: %d" %(i,num,acc))
            
            while l < i:
                if acc - nums[l] >= target:
                    # print("remove l %d: nums[l]: %d" %(l,nums[l]))
                    acc -= nums[l]
                    l += 1
                else:
                    break
            
            if acc >= target:
                if ret is None:
                    ret = i - l + 1
                else:
                    ret = min(ret, i - l + 1)
            
        return ret if ret is not None else 0
                    
                
                
        