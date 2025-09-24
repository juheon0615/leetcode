class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ["M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        ret = ""
        for i in range(len(integers)):
            if num == 0:
                break
            
            integer = integers[i]
            roman = romans[i]

            d = num // integer
            num = num % integer

            ret += roman * d

        return ret


        