class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        
        ret = -1
        
        queue = [startGene]
        visited = set()
        mutate = 0
        
        mutateDict = {"A" : "CGT", "C":"AGT", "G": "ACT", "T":"ACG" }
        
        while queue:
            nextQueue = []

            for i in range(len(queue)):
                gene = queue[i]
                # print(gene)
                if endGene == gene:
                    ret = mutate
                    break
                
                for j in range(len(gene)):
                    
                    mutables = mutateDict[gene[j]]
                    
                    for c in mutables:                        
                        mutatedGene = gene[:j] + c + gene[j+1:] 
                        # print(">>> ", mutatedGene)
                        if mutatedGene in bank and mutatedGene not in visited:
                            visited.add(mutatedGene)
                            nextQueue.append(mutatedGene)
            if ret != -1:
                break
            # print(nextQueue)
            queue = nextQueue
            mutate += 1

        
        return ret
        