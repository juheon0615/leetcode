class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj = None
        
        for num in nums:
            if count == 0:
                maj = num
                count += 1
            else:
                if num == maj:
                    count += 1
                else:
                    count -= 1
        
        return maj
        
        
        