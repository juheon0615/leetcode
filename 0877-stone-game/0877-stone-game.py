class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def dp(l, r, alice, mem):
            if l > r:
                return 0
            
            if (l,r) in mem:
                return mem[(l,r)]
            
            ret = None
            
            if alice == True:
                ret = max(dp(l+1, r, False, mem) + piles[l], dp(l, r - 1, False, mem) + piles[r])
            else:
                ret =  min(dp(l+1, r, True, mem), dp(l, r-1, True, mem))
            
            mem[(l,r)] = ret
            return mem[(l,r)]
        
        
        score = dp(0, len(piles) - 1, True, {})
        
        
        return True if score > (sum(piles) // 2) else False
            
            
            
            
            
            
            
            
            
        
        