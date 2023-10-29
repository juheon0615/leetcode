class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        this approach can use hashmap to keep the count of num at i 
        and find if k-i exist in the hashmap
        are there negative numbers?
        
        '''
        
        ret = 0
        counter = Counter(nums)
        for num in nums:
            if counter[num] > 0:
                target = k - num
                
                if target == num:
                    if counter[num] > 1:
                        counter[num] -= 2
                        ret += 1
                else:
                    if target in counter and counter[target] > 0:
                        counter[num] -= 1
                        counter[target] -= 1
                        ret += 1
        
        return ret
                    
                