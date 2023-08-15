class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = {}
        
        for num in arr:
            if num not in nums:
                nums[num] = 0
            
            nums[num] += 1
        
        
        occurence = set()
        for num, cnt in nums.items():
            occurence.add(cnt)
            
        
        return True if len(occurence) == len(nums) else False
            
        