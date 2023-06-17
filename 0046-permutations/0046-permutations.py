class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#         ret = []
        
#         def dfs(nums, cur):
#             if len(nums) == 0:
#                 ret.append(cur)
#                 return
#             for i in range(len(nums)):
#                 dfs(nums[:i] + nums[i+1:], cur[:] + [nums[i]])
        
#         dfs(nums,[])
        # using counter for memory
    
    
    
        ret = []
        def dfs(counter, cur):
            if len(cur) == len(nums):
                ret.append(cur)
                return
            
            for x in counter:
                if counter[x] > 0:
                    counter[x] -= 1
                    dfs(counter, cur + [x])
                    counter[x] += 1
              
        dfs(Counter(nums), [])
                
        return ret
                
                