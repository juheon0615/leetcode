class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                if stack[-1][0] < temp:
                    t, j = stack.pop()
                    ret[j] = i - j
            stack.append([temp, i])
        
        return ret
        