class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 여러 구간이 있는지 질문
        # 소팅이 안된 시작구간 찾기. ith > i+1th
        # 안된 시작 구간의 i 를 기억
        # 저장된 ith 보다 큰 수를 k 에서 찾으면 k-1이 소팅 안된구간의 종료 지점, 만약 리스트의 
        # 끝이라면 unsorted range = [x, nums.end]
        # 소팅 안된구간동안 가장 작은 수 mm를 기억.
        # 다시 리스트 시작부터 mm보다 큰 수를 찾음... 큰 수를 찾은 곳이 구간의 start
        # 구간을 하나로 머지한다. [min start, max end] 
        
        unsorteds = []
        start = end = None
        rangeMin = math.inf
        
        
        for i in range(1, len(nums)):
            if start is not None:
                if nums[start] <= nums[i]:
                    end = i - 1
                    
                    unsorteds.append((start,end, rangeMin))
                    start = None
                    end = None
                    rangeMin = math.inf
                else:
                    rangeMin = min(rangeMin, nums[i])
            else:
                if nums[i-1] > nums[i]:
                    start = i - 1
                    rangeMin = nums[i]
        
        if start is not None and end is None:
            unsorteds.append((start,len(nums)-1, rangeMin))
        
        if len(unsorteds) == 0:
            return 0
        
        adjusted = []
        
        start, end, rangeMin = math.inf, -math.inf, math.inf
        
        for unsorted in unsorteds:
            us, ue, um = unsorted
            
            start = min(start,us)
            end = max(end, ue)
            rangeMin = min(rangeMin, um)
    
            
        print(unsorteds)
        print(start," : ", end, " : ", rangeMin)
        
        for i in range(0, start):
            if nums[i] > rangeMin:
                start = i
                break
                
        print(start," : ", end)
        return end - start + 1
        
                
                
                