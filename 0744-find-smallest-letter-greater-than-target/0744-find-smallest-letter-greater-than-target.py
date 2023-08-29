class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        ret = None
        
        for c in letters:
            if c > target:
                ret = c
                break
        
        return ret if ret is not None else letters[0]
        