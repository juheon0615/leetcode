class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.dc = {}
        self.q = []
        self.entry = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        #print(self.q)

        if key not in self.d:
            return -1
        
        heapq.heappush(self.q, (self.entry, key))
        self.dc[key] += 1
        self.entry += 1
        return self.d[key]
        
    def put(self, key: int, value: int) -> None:
        #print(self.q)
        if key in self.d:
            self.d[key] = value
            self.dc[key] += 1
            heapq.heappush(self.q, (self.entry, key))
            self.entry += 1
            return
        
        while len(self.d) == self.capacity:
            _, k = heapq.heappop(self.q)
            
            self.dc[k] -= 1
            if self.dc[k] == 0:
                self.dc.pop(k)
                self.d.pop(k)
            
        self.d[key] = value
        self.dc[key] = 1
        
        heapq.heappush(self.q, (self.entry, key))
        self.entry += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)