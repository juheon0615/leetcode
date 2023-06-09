class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        
        for j, num in enumerate(arr):
            if  abs(arr[i] - x) > abs(arr[j] - x):
                i = j
        
        if k == 1:
            return [arr[i]]
        
        l = r = i
        
        while r - l < k - 1:
            # print("l %d i %d r %d" %(l,i,r))
            if r == len(arr) - 1:
                l -= 1
            elif l == 0:
                r += 1
            else:
                if abs(arr[l-1] - x) > abs(arr[r+1] - x):
                    r += 1
                elif abs(arr[l-1] - x) < abs(arr[r+1] - x):
                    l -= 1
                else:
                    if arr[l-1] <= arr[r+1]:
                        l -= 1
                    else:
                        r += 1
        
        
        return arr[l:r+1]
        