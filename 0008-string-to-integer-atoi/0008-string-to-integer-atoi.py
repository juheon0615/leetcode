class Solution:
    def myAtoi(self, s: str) -> int:
        
        integerString = ""
        hasDigit = False
        for ch in s:
            if ch.isnumeric():
                integerString += ch
                hasDigit = True
            elif ch == "-" or ch == "+":
                if hasDigit == False:
                    integerString += ch
                    hasDigit = True
                else:
                    break
            else:
                if hasDigit == False and ch == " ":
                    continue
                else:
                    break
        
        ret = 0
        if integerString != "-" and integerString != "+" and integerString != "":
            ret = int(integerString)
        
        ret = pow(2,31) - 1 if ret > pow(2,31) - 1 else ret
        ret = -pow(2,31) if ret < -pow(2,31) else ret

        
        
        return 0 if ret == "" else int(ret)
            
            
        
        