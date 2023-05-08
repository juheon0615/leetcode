class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = []
        visited = set()
        ret = False
        
        q.append(0)
        visited.add(0)
        while q:
            i = q.pop(0)
            j = nums[i]
            
            if i + j >= len(nums) - 1:
                ret = True
                break
            else:
                for jj in range(j):
                    ii = i + jj + 1
                    if ii not in visited:
                        q.append(ii)
                        visited.add(ii)
            
            
         
        return ret
        
        