class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        val = 0
        ret = 0
        
        for i, num in enumerate(nums):
            right = i
            val += num
            print(i)
            if val >= target:
                while val - nums[left] >= target and left <= right:
                    val -= nums[left]
                    left += 1
                
                # print(">> update ret %d left %d right %d" % (ret, left, right) )

                if ret > 0:
                    ret = min(ret, right - left + 1)
                else:
                    ret = right - left + 1
            
        
        return ret

                
                
        