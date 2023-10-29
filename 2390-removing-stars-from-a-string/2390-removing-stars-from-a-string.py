class Solution:
    def removeStars(self, s: str) -> str:
        
        '''
        object, remove character next to "*"
        if there is no char next * just remove the start
        
        stack can be applied
        push until *, pop if stack size bigger than 0
        
        return reversed and joined
        '''
        
        stack = []
        
        for c in s:
            if c == "*":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(c)
        
        return "".join(stack)
        