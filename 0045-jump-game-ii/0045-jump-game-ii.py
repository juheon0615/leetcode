class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = {}
        def dp(idx):
            # print(idx)
            if idx in visited:
                return visited[idx]
            
            if idx == len(nums) - 1:
                return 1
            
            if idx >= len(nums):
                return -1
            
            ret = -1
            
            for i in range(1, nums[idx] + 1):
                r = dp(idx + i)
                if r > 0:
                    if ret == -1:
                        ret = r
                    else:
                        ret = min(ret, r)
            
            ret = ret if ret == -1 else ret + 1
            visited[idx] = ret
            
            return ret
            
        ret = dp(0)
        # print(visited)
        return ret - 1
        