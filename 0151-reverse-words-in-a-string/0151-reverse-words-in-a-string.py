class Solution:
    def reverseWords(self, s: str) -> str:
        
        splits = s.split(" ")
        words = []
        
        for i in range(len(splits)):
            stripped = splits[i].strip()
            
            if stripped != "":
                words.append(stripped)
        
        ret = ""
        
        # print(words)
        for i in range(len(words) - 1, -1, -1):
            if words[i] == "":
                continue
            ret += words[i]
            if i > 0:
                ret += " "
        
        return ret
        