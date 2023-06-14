class Solution:
    def countAndSay(self, n: int) -> str:
        def countAndSay(nStr):
            say = ""
            prev = None
            prevCnt = 0

            for d in nStr:
                if prev is None:
                    prev = d
                    prevCnt = 1
                elif d == prev:
                    prevCnt += 1
                else:
                    say += str(prevCnt)
                    say += prev
                    prev = d
                    prevCnt = 1

            if prev is not None:
                say += str(prevCnt)
                say += prev
        
            return say
        
        ret = str(1)
        for i in range(n-1):
            ret = countAndSay(ret)
            
        
        return ret
        