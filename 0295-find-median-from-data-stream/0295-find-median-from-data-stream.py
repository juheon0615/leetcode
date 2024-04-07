class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        return self.nums[len(self.nums)//2] if len(self.nums) % 2 != 0 else (self.nums[len(self.nums)//2] + self.nums[len(self.nums)//2 -1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()