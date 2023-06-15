class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        def dfs(idx, cur, total):
            if total == target:
                ret.append(cur)
                return
            
            if total > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                dfs(i+1, cur + [candidates[i]], total + candidates[i])
        
        dfs(0, [], 0)
        return ret
            
                    
            
        