class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        mem = [[-1 for _ in range(len(nums))] for __ in range(len(nums))]
        
        def predict(left, right):
            if left > right or left >= len(nums) or right < 0:
                return 0
            
            if mem[left][right] != -1:
                return mem[left][right]
            
            takeRight = nums[right] + min(predict(left + 1, right - 1), 
                      predict(left, right - 2))
            takeLeft = nums[left] + min(predict(left + 1, right - 1), 
                      predict(left + 2, right))
            
            # print("left %d right %d" % (takeLeft, takeRight))
            ret = max(takeLeft, takeRight)
                
                      
            mem[left][right] = ret
            return mem[left][right]
        
        
        maxS1 = predict(0, len(nums)-1)
        # print(mem)
        return maxS1 >= (sum(nums) - maxS1)
        