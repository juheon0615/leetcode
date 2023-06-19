class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1 for _ in range(len(nums))]
        
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                # print("i : ", i , " j: ", j, "  ", lis)
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        
        
        ret = lis[0]
        
        for n in lis:
            if n > ret:
                ret = n
        
        return ret
                
        
        
#         answer = 0
#         mem = [[-1 for prev in range(len(nums) + 1)] for i in range(len(nums))]
#         def dp(i, prev):
#             if i == len(nums):
#                 return 0
            
#             if mem[i][prev+1] != -1:
#                 return mem[i][prev+1]
            
#             ret = dp(i + 1, prev)
#             if prev == -1 or nums[i] > nums[prev]:
#                 ret = max(ret, dp(i + 1, i) + 1)
            
#             mem[i][prev+1] = ret
            
#             return ret 
        
#         answer = dp(0,-1)
        
#         return answer
        
        
            
        