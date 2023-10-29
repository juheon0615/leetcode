class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        what happes if asteroid heading left is at i and right is at i + 1?
        what happend if size is the same? both explose
        zero? none
        
        stack approach can be applied
        
        a = asteroid. can be either + or -
        
        if stack is none: append(a)
        
        if stack is not None: check if direction is different
        
        if stack top is + and new a is -:
        pop if abs(top) > conintue
        if == pop and continue
        if abs(top) < a: 
        pop until abs(top) >= a 
        '''
        stack = []
        
        for a in asteroids:
            # print(stack)
            if len(stack) > 0 and (stack[-1] > 0 and a < 0):    
                #remove all small colliding astroid from stack
                while stack and (stack[-1] > 0 and a < 0) and abs(stack[-1]) < abs(a):
                    stack.pop(-1)
                    
                # if stack is empty or same direction push
                if len(stack) > 0 and (stack[-1] > 0 and a < 0):
                    if abs(stack[-1]) > abs(a):
                        pass
                    elif abs(stack[-1]) == abs(a):
                        stack.pop(-1)
                else:
                    stack.append(a)
            else:
                stack.append(a)
        
        return stack
                
                