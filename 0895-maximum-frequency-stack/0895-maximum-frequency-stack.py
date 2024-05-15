class FreqStack:

    def __init__(self):
        self.counts = {} 
        self.stackAtCount = {}
        self.curMax = 0
        
    def push(self, val: int) -> None:
        if val not in self.counts:
            self.counts[val] = 0
        
        self.counts[val] += 1
        
        if self.counts[val] > self.curMax:
            self.curMax = self.counts[val]
        
        if self.counts[val] not in self.stackAtCount:
            self.stackAtCount[self.counts[val]] = []
        
        self.stackAtCount[self.counts[val]].append(val)
        
    def pop(self) -> int:
        val = self.stackAtCount[self.curMax].pop()
        self.counts[val] -= 1
        
        
        if len(self.stackAtCount[self.curMax]) == 0:
            self.curMax -= 1
        
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()