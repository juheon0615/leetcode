class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = {}
        ret = 0
        for num in nums:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1
        
        for num in nums:
            if k <= num:
                continue
            
            diff = k - num

            if diff == num:
                if hmap[num] > 1:
                    hmap[num] -= 2
                    ret += 1
            else:
                if diff in hmap and hmap[diff] > 0 and hmap[num] > 0:
                    hmap[num] -= 1
                    hmap[diff] -= 1
                    ret += 1
        return ret


        # '''
        # this approach can use hashmap to keep the count of num at i 
        # and find if k-i exist in the hashmap
        # are there negative numbers?
        
        # '''
        
        # ret = 0
        # counter = Counter(nums)
        # for num in nums:
        #     if counter[num] > 0:
        #         target = k - num
                
        #         if target == num:
        #             if counter[num] > 1:
        #                 counter[num] -= 2
        #                 ret += 1
        #         else:
        #             if target in counter and counter[target] > 0:
        #                 counter[num] -= 1
        #                 counter[target] -= 1
        #                 ret += 1
        
        # return ret
                    
                