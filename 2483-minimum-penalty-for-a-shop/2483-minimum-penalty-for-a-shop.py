class Solution:
    def bestClosingTime(self, customers: str) -> int:
        Y = 0
        for c in customers:
            if c == "Y":
                Y += 1
        
        
        N = 0
        
        ret = 0
        minP = Y - N 
        
        for i, c in enumerate(customers):
            p = Y + N 
            
            # print(i , " : ", p)
            if p < minP:
                ret = i
                minP = p
                
            if c == "N":
                N += 1
            else:
                Y -= 1
        
        p = Y + N 
        if p < minP:
            ret = len(customers)
            minP = p
        return ret
        
    

    
        