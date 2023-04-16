class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cntA = [0] * 7
        cntB = [0] * 7
        cntSame = [0] * 7
        for i in range(len(tops)):
            a, b = tops[i], bottoms[i]
            cntA[a] += 1
            cntB[b] += 1
            if a == b: cntSame[a] += 1
        ans = len(tops)
        for v in range(1, 7):
            aOnly = cntA[v] - cntSame[v]
            bOnly = cntB[v] - cntSame[v]
            
            if aOnly + bOnly + cntSame[v] == len(tops):
                minSwap = min(aOnly, bOnly)
                ans = min(ans, minSwap)
                
        return -1 if ans == len(tops) else ans
            
        