class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for n in num:
            
            while stack and int(n) < int(stack[-1]) and k > 0:
                stack.pop(-1)
                k -= 1
            
            if stack or n != '0':
                stack.append(n)
        
        if k > 0:
            stack = stack[0:-k]
        
        if len(stack) == 0:
            stack.append("0")
        return "".join(stack)
        
        
        