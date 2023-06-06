class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        cur = 0
        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)
                nums[cur] = num
                cur += 1

        return len(seen)
        