class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = digits[:]
        
        carry = False
        for i in range(len(ret) - 1, -1, -1):
            if ret[i] == 9:
                ret[i] = 0
                carry = True
            else:
                ret[i] += 1
                carry = False
            
            if carry == False:
                break
        
        if carry is True:
            ret = [1] + ret
        
        
        return ret
            
        