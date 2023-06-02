class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        ret = ""
        while num > 0:
            for i, val in enumerate(vals):
                if num >= val:
                    mult = num // val
                    ret += (syms[i] * mult)
                    num -= (val * mult)
                    
                    
        
        return ret
        