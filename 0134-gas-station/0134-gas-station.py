class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        nets = [gas[i] - cost[i] for i in range(n)]

        if sum(nets) < 0:
            return -1
        
        acc = 0
        ret = None
        for i in range(n):
            if acc + nets[i] >= 0:
                # dont update
                ret = i if ret is None else ret
                acc += nets[i]
            else:
                ret = None
                acc = 0


        print(nets)
        return ret
        