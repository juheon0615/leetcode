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

        for i, ch in enumerate(s):
            if ch == "*" and stack:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

        