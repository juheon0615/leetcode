class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.numbers = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        self.pos[val] = len(self.numbers)
        self.numbers.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        idx = self.pos[val]
        last = self.numbers[-1]

        self.numbers[idx] = last
        self.pos[last] = idx
        self.numbers.pop()
        del self.pos[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()