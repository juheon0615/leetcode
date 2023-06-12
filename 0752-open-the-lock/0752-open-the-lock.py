class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        queue = []
        visited = set()
        
        if "0000" in deadends:
            return -1
        
        queue.append("0000")
        visited.add("0000")
        
        moves = 0
        found = False
        while queue:
            nextQueue = []
            
            while queue:
                comb = queue.pop()
                if comb == target:
                    found = True
                    break
            
                
                for i, d in enumerate(comb):
                    dr = dl = d

                    
                    if d == "9":
                        dr = "0"
                        dl = "8"
                    elif d == "0":
                        dr = "1"
                        dl = "9"
                    else:
                        dr = str(int(d) + 1)
                        dl = str(int(d) - 1)
                    
                    combRight = comb[:i] + dr + comb[i + 1:]
                    combLeft = comb[:i] + dl + comb[i + 1:]


                    
                    if combRight not in visited and combRight not in deadends:
                        nextQueue.append(combRight)
                        visited.add(combRight)
                        
                    if combLeft not in visited and combLeft not in deadends:
                        nextQueue.append(combLeft)
                        visited.add(combLeft)
                                            
            if found:
                break
                
            queue = nextQueue
            moves += 1
        
        return moves if found else -1
            
            
            
            