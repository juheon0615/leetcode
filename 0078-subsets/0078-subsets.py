class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []

        
        counts = Counter(nums)

        def backtrack(cur, counts):
            ret.append(cur[:])
            # print(counts)
            # print(cur)
            # print(ret)
            for key in counts:
                if counts[key] > 0:
                    if len(cur) > 0 and cur[-1] > key:
                        continue
                    counts[key] -= 1
                    cur.append(key)
                    backtrack(cur, counts)
                    cur.pop()
                    counts[key] += 1


        backtrack([], counts)

        return ret        