class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        c = m * n


        lo = 0 
        hi = c


        while lo < hi:
            mid = (lo + hi) // 2
            row = mid // n 
            col = mid % n

            t = matrix[row][col]
            # print("matric[%d][%d] = %d hi: %d lo: %d " % (row, col, t, hi, lo))

            if t == target:
                return True
            
            if t > target:
                hi = mid
            else:
                lo = mid + 1
        return False
            