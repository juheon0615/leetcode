class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4] -> [2,4,1,3]
        '''
        ret = []
        for num in nums:
            if num % 2 == 0:
                ret.append(num)
        
        for num in nums:
            if num % 2 == 1:
                ret.append(num)
        
        return ret
        