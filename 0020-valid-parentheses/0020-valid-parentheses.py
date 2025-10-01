class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ["(", "[", "{"]
        closes = {")" : "(", "]" : "[", "}" : "{"}

        for b in s:
            if b in opens:
                stack.append(b)
            else:
                if len(stack) == 0 or stack[-1] != closes[b]:
                    return False
                else:
                    stack.pop()
        
        return True if len(stack) == 0 else False

        