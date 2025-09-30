class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = math.inf

        j = 0
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= target:
                ret = min(ret, i - j + 1)
                curSum -= nums[j]
                j += 1               
        return ret if ret != math.inf else 0


            
        

                
            
            
        