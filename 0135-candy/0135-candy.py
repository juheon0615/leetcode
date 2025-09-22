class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ltr = [1 for _ in range(n)]
        rtl = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ltr[i] = ltr[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rtl[i] = rtl[i+1] + 1
        
        maxArray = [ max(ltr[i], rtl[i]) for i in range(n)]

        # print(ltr)
        # print(rtl)
        # print(maxArray)
        return sum(maxArray)

        