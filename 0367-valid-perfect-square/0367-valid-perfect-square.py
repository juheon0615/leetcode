class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 1
        high = num // 2
        ret = False
        
        while low <= high:
            cur = ((low + high) // 2)
            
            if cur**2 == num:
                ret = True
                break
            elif cur**2 < num:
                if low == cur:
                    low += 1
                else:
                    low = cur
            else:
                if high == cur:
                    high -= 1
                else: 
                    high = cur
        
                    
        return ret
        