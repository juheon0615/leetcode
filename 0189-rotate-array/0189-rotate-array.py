class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cache = nums[:]

        for i in range(len(nums)):
            j = (i + k) % len(nums)
            nums[j] = cache[i]

        