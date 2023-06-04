class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8": "tuv", "9" : "wxyz"}
        
        ret = []
        curQueue = None
        
        for digit in digits:
            newQueue = [] 
            letters = pad[digit]

            if curQueue:
                for cur in curQueue:
                    for letter in letters:
                        newQueue.append(cur + letter)
            else:
                for letter in letters:
                    newQueue.append(letter)
                
            curQueue = newQueue
        
        if curQueue:
            ret = curQueue
            
        return ret