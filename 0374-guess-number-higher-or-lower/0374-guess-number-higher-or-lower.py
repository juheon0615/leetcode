# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        result = -1
        
        while left <= right:
            num = (right + left) // 2
            result = guess(num)
            
            if result == 0:
                return num
            elif result > 0:
                if num == left:
                    left += 1
                else:
                    left = num
            else:
                right = num
        
        return -1
                
            
        
        