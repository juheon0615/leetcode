class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0 # index to place new number
        prev = None
        cont = 0
        for j in range(len(nums)):
            # print(j, " : ", i, " : ", prev, " : ",cont)
            if prev is None:
                nums[i] = nums[j]
                prev = nums[j]
                cont = 1
                i += 1
            elif prev == nums[j]:
                if cont < 2:
                    nums[i] = nums[j]
                    cont += 1
                    i += 1
            else:
                prev = nums[j]
                nums[i] = nums[j]
                cont = 1
                prev = nums[j]
                i += 1
        print(nums)

        return i
        
        