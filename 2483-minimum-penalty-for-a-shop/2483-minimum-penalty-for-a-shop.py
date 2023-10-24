class Solution:
    def bestClosingTime(self, customers: str) -> int:        
        # penalty closing at i = i-1th open + ith close 
        # penalty closing at i = pOpen_i-1 + pClose_i
        
        # need to create pOpen and pClose
        
        n = len(customers)
        opens = [0 for _ in range(n + 1)]
        closes = [0 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            if customers[i] == "Y":
                closes[i] += 1
            closes[i] += closes[i+1]
        
        for i in range(n):
            if customers[i] == "N":
                opens[i] += 1
            if i > 0:
                opens[i] += opens[i-1]
        
        print(opens)
        print(closes)
        ret = 0
        minP = closes[0]
        
        for i in range(n):
            p = opens[i] + closes[i+1]
            
            if p < minP:
                ret = i + 1
                minP = p
            
        return ret
        
        
    

    
        