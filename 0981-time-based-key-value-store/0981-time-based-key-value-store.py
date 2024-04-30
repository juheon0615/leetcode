class TimeMap:

    def __init__(self):
        self._map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._map:
            self._map[key] = []
        self._map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:     
        if key not in self._map:
            return ""
        
        i = bisect.bisect_left(self._map[key], timestamp, key= lambda x:x[1])
        
        if i == len(self._map[key]):
            return self._map[key][-1][0]            
        
        if timestamp == self._map[key][i][1]:
            return self._map[key][i][0]
        elif timestamp < self._map[key][i][1]:
            if i == 0:
                return ""
            else:
                return self._map[key][i-1][0]
        
        
        
    
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)