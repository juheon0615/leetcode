class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return [nums[0]]
        
        num1 = None
        count1 = 0
        
        num2 = None
        count2 = 0
        
        for num in nums:

            
            if num == num1 or num == num2:
                if num == num1:
                    count1 += 1
                else:
                    count2 += 1
            elif count1 == 0 or count2 == 0:
                if count1 == 0:
                    num1 = num
                    count1 += 1
                else:
                    num2 = num
                    count2 += 1                
            else:
                count1 -= 1
                count2 -= 1
        
        
        output = []
        if nums.count(num1) > len(nums) // 3:
            output.append(num1)
        if nums.count(num2) > len(nums) // 3:
            output.append(num2)

        return output