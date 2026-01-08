class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = [] # this will form a number
        for n in num:
            while stack and int(n) < int(stack[-1]) and k > 0: 
                # will try to keep only smaller number from
                stack.pop()
                k -= 1
            stack.append(n)

            # append first then check if it need to be popped in the later index

        while k > 0:
            stack.pop()
            k -= 1

         
        
        if not stack:
            return "0"
        else:
            ret = "".join(stack).lstrip("0")
            return ret if ret else "0"
            
        

        




        