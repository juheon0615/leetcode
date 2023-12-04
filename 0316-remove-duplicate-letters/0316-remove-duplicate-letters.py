class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        counts = Counter(s)
        for c in s:
            counts[c] -= 1
            
            if c in stack:
                continue
            
            while stack and stack[-1] > c and counts[stack[-1]] > 0:
                stack.pop(-1)
            
            stack.append(c)
        
        return "".join(stack)
                    