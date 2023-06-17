class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         def dfs(counter, cur):
#             if len(cur) == len(nums):
#                 ret.append(cur)
#                 return
            
#             for x in counter:
#                 if counter[x] > 0:
#                     counter[x] -= 1
#                     dfs(counter, cur + [x])
#                     counter[x] += 1

        # dfs(Counter(nums), [])
        
        ret = []
        cnt = []
        def dfs(nums, cur):
            if len(nums) == 0:
                ret.append(cur)
                return
            
            dup = set()
            
            for i in range(len(nums)):
                if nums[i] in dup:
                    continue
                dup.add(nums[i])
                dfs(nums[:i] + nums[i+1:], cur[:] + [nums[i]])
        
        dfs(nums,[])

        return ret
        