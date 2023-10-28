class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        popCur = 0
        
        for n in pushed:
            stack.append(n)
            
            while stack and popCur < len(popped) and popped[popCur] == stack[-1]:
                stack.pop(-1)
                popCur += 1
        
        return True if len(stack) == 0 else False
            
            
        
        
        