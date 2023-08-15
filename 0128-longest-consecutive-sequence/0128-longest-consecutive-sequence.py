class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        ns = set()
        ret = 0
        
        for num in nums:
            ns.add(num)
        
        for num in ns:
            if num - 1 not in ns:
                k = 1
                while num + k in ns:
                    k += 1
            
                ret = max(ret, k)
        
        return ret