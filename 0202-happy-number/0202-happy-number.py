class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()
        
        num = n
        ret = False
        
        while num not in s:
            if num == 1:
                ret = True
                break
                
            s.add(num)
            nextNum = 0
            snum = str(num)
            for d in snum:
                nextNum += (pow(int(d), 2))
            
            num = nextNum
        return ret