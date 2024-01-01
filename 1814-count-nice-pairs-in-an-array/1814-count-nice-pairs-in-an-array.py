class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(x):
            return int(str(x)[::-1])
        
        N = len(nums)
        rnums = [rev(num) for num in nums]

        # nums[i] - rnums[i]
        diffs = [nums[i] - rnums[i] for i in range(N)]
        
        ret = 0
        
        pairs = {}
        
        for num in diffs:
            if num not in pairs:
                pairs[num] = 0
            pairs[num] += 1
            
        
        for count in pairs.values():
            ret += math.comb(count,2)
            ret %= (pow(10,9) + 7)
        
        
        return ret
            
        