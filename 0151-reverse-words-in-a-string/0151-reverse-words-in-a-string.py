class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        strippedWords = []
        for word in words:
            stripped = word.strip()
            if len(stripped) > 0:
                strippedWords.append(stripped)
        
        return " ".join(strippedWords)
