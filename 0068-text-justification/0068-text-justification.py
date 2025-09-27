class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        curWidth = 0
        curLine = []
        lines = []
        for word in words:
            if len(word) + curWidth + len(curLine) - 1 < maxWidth:
                curLine.append(word)
                curWidth += len(word) 
            else:
                lines.append([curLine, curWidth])
                curLine = []
                curWidth = len(word)
                curLine.append(word)
        
        if len(curLine) > 0:
            lines.append([curLine, curWidth])

        returnArray = []
        for i in range(len(lines)):
            line, width = lines[i]
            numWords = len(line)

            if i == len(lines) - 1:
                text = ""
                for j in range(len(line)):
                    if j == len(line) - 1:
                        text += line[j]
                        spacer = " " * (maxWidth- len(text))
                        text += spacer
                    else:
                        text += line[j] + " "
                returnArray.append(text)
            elif numWords == 1:
                spacer = " "  * (maxWidth - width)
                text = line[0] + spacer
                returnArray.append(text)
            else:
                spacerWidth = (maxWidth - width) // (numWords - 1)
                extraSpacerIndex = (maxWidth - width) % (numWords - 1)
                text = ""
                for j in range(len(line)):
                    if j == len(line) - 1:
                        text += line[j]
                    else:
                        spacer = " " * spacerWidth
                        text += line[j] + spacer
                    
                    if j < extraSpacerIndex:
                        text += " "
                returnArray.append(text)



        return returnArray

            
        
        