class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ret = ""
        words = s.split(" ")
        words = words[::-1]

        for i, word in enumerate(words):
            stripped = word.strip()
            if len(stripped) > 0:
                ret += stripped
                if i != len(words) - 1:
                    ret += " "
        
        return ret
        