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
            curLevel = queue[:]
            queue = []

            for cur in curLevel:
                if cur == target:
                    return ret
                
                for i in range(4):
                    turns = [-1, 1]
                    for t in turns:
                        nith = (int(cur[i]) + t) % 10
                        turned = cur[0:i] + str(nith) + cur[i+1: 4]

                        if turned not in deadends and turned not in visited:
                            queue.append(turned)
                            visited.add(turned)
            ret += 1
        return -1
        