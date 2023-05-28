class Solution:
    def myAtoi(self, s: str) -> int:
        #parse number
        
        num = ""
        s = s.lstrip(" ")
        hasSign = False
        hasNumber = False
        for c in s:
            if c.isnumeric():
                num += c
                hasNumber = True
            elif (c == "-" or c == "+") and hasNumber == False and hasSign == False:
                hasSign = True
                num += c
            else:
                break
        
        if hasNumber == False:
            num = "0"
        
        ret = int(num)
        
        
        if ret > pow(2,31) - 1:
            ret = pow(2,31) - 1
        
        if ret < pow(-2,31):
            ret = pow(-2,31)
            
        return ret