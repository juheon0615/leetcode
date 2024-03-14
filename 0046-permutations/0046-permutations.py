class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def backtrack(curs):
            if len(curs) == len(nums):
                ans.append(curs[:])
                return
            
            for num in nums:
                if num not in curs:
                    curs.append(num)
                    backtrack(curs)
                    curs.pop()
            
        backtrack([])
        return ans
                
                
                