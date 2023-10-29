class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        using a prev variable and last available index for list should solve this problem
        
        iterate chars
        if prev is None, prev will char and prevCount will be 1
        if prev is equal to char, prevCount will be incremented by 1
        if prev is not equal to char, chars[lastUsedIndex] = prev, last available index+= 1 \
        and if prev Count is > 1, chars[lastUsedIndex] = str(prev Count), lastUsedIndex += 1
        
        '''
        
        availableIndex = 0
        prevChar = None
        prevCount = 0
        
        for c in chars:
            if prevChar is None:
                prevChar = c
                prevCount += 1
            elif prevChar == c:
                prevCount += 1
            else:
                chars[availableIndex] = prevChar
                availableIndex += 1
    
                if prevCount > 1:
                    strPrevCount = str(prevCount)
                    for digit in strPrevCount:
                        chars[availableIndex] = digit
                        availableIndex += 1
                
                prevChar = c
                prevCount = 1
        
        if prevChar is not None:
            chars[availableIndex] = prevChar
            availableIndex += 1
    
            if prevCount > 1:
                strPrevCount = str(prevCount)
                for digit in strPrevCount:
                    chars[availableIndex] = digit
                    availableIndex += 1
                
        return availableIndex            
                    