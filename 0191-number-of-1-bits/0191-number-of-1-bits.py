class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ret = 0
        bs = "{0:b}".format(n)

        for b in bs:
            if b == '1':
                ret += 1
        
        return ret