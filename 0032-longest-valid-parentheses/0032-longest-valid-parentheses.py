class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        idea... keep the index of incomplete parentheses
        calculate the largest diff between the incomplete parentheses
        '''
        
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if len(stack) > 0 and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

        if len(stack) == 0:
            return len(s)
        
        ret = 0
        n = len(s)
        while stack:
            ret = max(ret, n - stack[-1] - 1)
            n = stack.pop()
        
        return max(ret, n)
