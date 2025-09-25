class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        lastWord = words[-1].strip()

        return len(lastWord)
        