class Solution:
    def decodeString(self, s: str) -> str:
        '''
        stack 
        
        "["
        push until "]"
        pop unil "[", add to estring
        pop until top not num, 
        push num * estring
        '''
        
        stack = []
        
        for c in s:
            if c == "]":
                eString = ""
                while stack[-1] != "[":
                    eString += stack.pop(-1)
                stack.pop(-1)
                eString = eString[::-1]
                
                eNumString = ""
                while stack and stack[-1].isnumeric() == True:
                    eNumString += stack.pop(-1)
                
                eNumString = eNumString[::-1]

                eString = eString * int(eNumString)
                
                for e in eString:
                    stack.append(e)
            else:
                stack.append(c)
        
        ret = ""
        for encoded in stack:
            ret += encoded
        
        return ret
        