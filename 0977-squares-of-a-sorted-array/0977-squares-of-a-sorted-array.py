class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        cnts = [0 for _ in range(pow(10,4) + 1)]
        
        for num in nums:
            if num < 0:
                num = abs(num)
            cnts[num] += 1
        
        ret = []
        
        for i in range(len(cnts)):
            for c in range(cnts[i]):
                ret.append(pow(i,2))
        
        return ret
        
        