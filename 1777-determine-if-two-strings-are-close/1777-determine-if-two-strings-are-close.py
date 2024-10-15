class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        two rules
        1. same unique char
        2. same frequency distribution
        '''

        set1 = set(word1)
        set2 = set(word2)

        if set1 != set2:
            return False
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        
        return True
        
            