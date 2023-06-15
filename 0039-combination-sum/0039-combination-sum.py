class Solution:
    def dfs(self, nums, cur, target, ret):
        if target == 0:
            ret.append(cur)
            return

        if target < 0:
            return


        for i, num in enumerate(nums):
            self.dfs(nums[i:], cur[:] + [nums[i]], target - nums[i], ret)
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # ret = []
        # self.dfs(candidates, [], target, ret)
        
        ret = []
        q = []
        
        # [current start i, cur comb, remaining target]
        
        q.append([0, [], target])
        while q:
            nextQ = []
            
            while q:
                c = q.pop()
                i = c[0]
                comb = c[1]
                t = c[2]
                
                if c[2] == 0:
                    ret.append(c[1])
                elif c[2] < 0 :
                    continue
                else:
                    for j in range(i, len(candidates)):
                        nextQ.append([j, comb[:] + [candidates[j]], t - candidates[j]])
            
            q = nextQ


        return ret
            