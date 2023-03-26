class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        else:
            self.d[val] = len(self.vals)
            self.vals.append(val)
            return True
                

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        else:
            # Swap
            curLastVal = self.vals[-1]
            
            rmIdx = self.d[val]
            
            self.vals[rmIdx] = curLastVal
            self.d[curLastVal] = rmIdx
            
            self.vals.pop(-1)
            del self.d[val]
            return True
        
    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()