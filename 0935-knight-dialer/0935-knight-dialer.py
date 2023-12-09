class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        if start is different, cannot be a same number
        at n, with num i can be memoized
        5 is unreachable to begin with
        '''
        
        def dial(n, cur):
            if (n,cur) in visited:
                return visited[(n,cur)]
            
            if n == 0:
                return 1
            
            ret = 0
            for num in nums[cur]:
                ret += dial(n-1, num)
            
            visited[(n,cur)] = ret
            return visited[(n,cur)]
        
        visited = {}
        nums = { 0:[4,6], 1 : [6,8], 2: [7,9], 3:[4,8], 4: [3,9,0], 6: [1,7,0], 7: [2,6], 8: [1,3], 9 : [2,4]}
        
        ret = 0
        if n == 1:
            return 10
        
        for start in nums.keys():
            ret += dial(n-1,start)
            ret = ret % (10 ** 9 + 7)
        
        
        return ret
        
        
            
            
            
        