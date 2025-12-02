class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        queue = []
        visited = set()

        if start not in deadends:
            queue.append(start)
            visited.add("0000")
        ret = 0
        while queue:
            # print(queue)
            nextLevel = []

            for cur in queue:
                if cur == target:
                    return ret
                
                for i in range(4):
                    turns = [-1, 1]
                    for t in turns:
                        nith = (int(cur[i]) + t) % 10
                        turned = cur[0:i] + str(nith) + cur[i+1: 4]

                        if turned not in deadends and turned not in visited:
                            nextLevel.append(turned)
                            visited.add(turned)
            ret += 1
            queue = nextLevel
        return -1
        