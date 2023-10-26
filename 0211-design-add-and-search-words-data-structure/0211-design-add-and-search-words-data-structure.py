class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.words = set()
    def addWord(self, word: str) -> None:
        self.words.add(word)
        t = self.trie
        for i, w in enumerate(word):
            if w in t:
                t = t[w]
            else:
                t[w] = {}
                t = t[w]
            if i == len(word) - 1:
                t["end"] = True
        

    def search(self, word: str) -> bool:
        def searchDfs(trie, word):
            # print(trie, " : ", word)
            if len(word) == 0:
                key = "end"
                return True if key in trie else False


            ret = False

            if word[0] == ".":
                for key in trie:
                    if key == "end":
                        continue
                    ret = ret or searchDfs(trie[key], word[1:])
            else:
                if word[0] in trie:
                    ret = searchDfs(trie[word[0]], word[1:])

            return ret
        
        return searchDfs(self.trie, word)
                    

        
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)