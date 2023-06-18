class Solution:
    def climbStairs(self, n: int) -> int:
        fib = []
        fib.append(0)
        fib.append(1)
        fib.append(2)
        
        for i in range(3, n+1):
            fib.append(fib[i-1] + fib[i-2])
        
        return fib[n]
            
        
#         mem = {}
#         def dp(n):
#             if n in mem:
#                 return mem[n]
            
#             if n == 0:
#                 return 1
            
#             if n < 0:
#                 return 0
            
#             ret = 0
#             for i in range(1, 3):
#                 ret += dp(n - i)
            
            
#             mem[n] = ret
#             return ret
    
#         return dp(n)
        
        
                