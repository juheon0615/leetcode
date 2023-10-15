class Solution:#57
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        specification to clairfy
        1. about the inputs. i.e if word is always shorter than maxWidth
        2. what if only one word can fit in the text? how do you space it?
        '''
        
        texts = []
        cur = ""
        for word in words:
            if len(cur) == 0:
                cur = word
            else:
                if len(cur) + len(word) + 1 <= maxWidth:
                    cur += " " + word
                else:
                    texts.append(cur)
                    cur = word
        texts.append(cur)
        # print(texts)
        for i, text in enumerate(texts):
            if i == len(texts) - 1:
                texts[i] = text + ((maxWidth - len(text)) * " ")
            else:
                if len(text) < maxWidth:                
                    words = text.split(" ")

                    if len(words) == 1:
                        texts[i] = words[0] + (" " * (maxWidth - len(text)))
                    else:
                        spaces = maxWidth - len(text) + len(words) - 1

                        distribute = spaces // (len(words) - 1)
                        remainder = spaces % (len(words) - 1)

                        adjusted = ""
                        for j in range(len(words)):
                            if j == len(words) - 1:
                                adjusted += words[j]
                            else:
                                adjusted += (words[j] + (" " * distribute))
                                if j < remainder:
                                    adjusted += " "
                        texts[i] = adjusted
            
        # print(texts)
        return texts
                        
                        
                    
                    
                
                
                
                
                    
                
                
            