class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        q = [(p,(0, p)) for p in primes]
        
        heapq.heapify(q)
        
        ret = [1]
        rset = set()
        while len(ret) < n:
            num, ii = heapq.heappop(q)
            i, p = ii
            if num not in rset:
                rset.add(num)
                ret.append(num)
            i += 1
            num = p * ret[i]
            heapq.heappush(q,(num, (i,p)))
        # print(q)
        # print(ret)
        return ret[-1]
        
        
        
        
# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
#         size = len(primes)
#         ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
#         for i in range(1, n):
#             # compute possibly ugly numbers and update index
#             for j in range(0, size):
#                 if ugly_nums[j] == ugly:
#                     ugly_nums[j] = dp[index[j]] * primes[j]
#                     index[j] += 1
#             # get the minimum
#             ugly = min(ugly_nums)
#             dp.append(ugly)
#         print(dp)
#         return dp[-1]
        
        