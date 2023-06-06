class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0
        
        for num in nums:
            if num == val:
                continue
            else:
                nums[cur] = num
                cur += 1
        
        
        return cur if cur > 0 else 0