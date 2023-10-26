class Trie:

    def __init__(self):
        self.trie = set()
        self.words = set()
        
    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            self.trie.add(word[0:i+1])
        

    def search(self, word: str) -> bool:
        return True if word in self.words else False
        

    def startsWith(self, prefix: str) -> bool:
        return True if prefix in self.trie else False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)