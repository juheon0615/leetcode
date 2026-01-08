class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #indexs
        N = len(temperatures)
        ret = [0 for _ in range(N)]
        
        for i in range(N):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ret[j] = i - j
            stack.append(i)
        
        return ret

        