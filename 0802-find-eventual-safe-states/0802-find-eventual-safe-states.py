class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        sets = []
        terminals = set()
        
        for i, edges in enumerate(graph):
            sets.append(set())
            
            for e in edges:
                sets[i].add(e)
            
            if len(sets[i]) == 0:
                terminals.add(i)
        
        
        added = True
        
        while True:
            added = False
            for i, edges in enumerate(sets):
                
                if i in terminals:
                    continue
                
                isSafeNode = True
                
                for e in edges:
                    if e not in terminals:
                        isSafeNode = False
                
                if isSafeNode:
                    terminals.add(i)
                    added = True                    
            
            if added == False:
                break
        
        
        ret = []
        for t in terminals:
            ret.append(t)
                
        ret.sort()
        return ret
            
        
        
            
            
        