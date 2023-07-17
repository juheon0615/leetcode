class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # bfs
        ret = []
        q = [(-1,[])]
        
        nums.sort()
        while q:
            nextQ = []
            while q:
                i, path = q.pop(0)
                ret.append(path)
                
                for j in range(i+1, len(nums)):
                    if j > i+1 and nums[j] == nums[j - 1]:
                        continue

                    newPath = path[:]
                    newPath.append(nums[j])
                    nextQ.append((j, newPath))
            
            q = nextQ
                    
            
            
        return ret
            
            
        