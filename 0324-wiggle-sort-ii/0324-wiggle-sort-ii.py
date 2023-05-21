class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        snums = []
        cnts = {}
        for num in nums:
            if num in cnts:
                cnts[num] += 1
            else:
                cnts[num] = 1
        
        for i in range(5001):
            if i in cnts:
                for j in range(cnts[i]):
                    snums.append(i)
        
        cur1 = len(nums) // 2
        if len(nums) % 2 == 0:
            cur1 -= 1
        cur2 = len(nums) - 1
        
        w = True
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = snums[cur1]
                cur1 -= 1
            else:
                nums[i] = snums[cur2]
                cur2 -= 1

            

        
        
        