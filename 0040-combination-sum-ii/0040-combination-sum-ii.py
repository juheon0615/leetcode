class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, t, cur, curStr, visited, ret):            
            if curStr in visited:
                return
            else:
                visited.add(curStr)
            
            if t == 0:
                ret.append(cur)
                return
            
            if t < 0:
                return
            
            for i in range(len(nums)-1):
                nextNum = nums[i+1]
                dfs(nums[i + 1:], t - nextNum, cur[:] + [nextNum], curStr + " " + str(nextNum), visited, ret)
            
        candidates.sort()
        nums = [0] + candidates[:]
        visited = set()
        ret = []

        dfs(nums, target, [], "", visited, ret)
        return ret
            
                    
            
        