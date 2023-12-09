class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret = 0
        
        counts = Counter(chars)
        
        for word in words:
            ccounts = dict(counts)
            canForm = True
            for w in word:
                if w in ccounts and ccounts[w] > 0:
                    ccounts[w] -= 1
                else:
                    canForm = False
                    break
            
            if canForm:
                ret += len(word)
        
        return ret
                    
                
            
        
        