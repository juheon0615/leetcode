class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        H = len(triangle)
        W = len(triangle[-1])

        for i in range(1, H):
            w = len(triangle[i])

            for j in range(w):
                prevMin = 0
                if j == 0:
                    prevMin = triangle[i-1][j]
                elif j == w - 1:
                    prevMin = triangle[i-1][j-1]
                else:
                    prevMin = min(triangle[i-1][j-1], triangle[i-1][j])
                
                triangle[i][j] += prevMin
        # print(triangle)
        return min(triangle[-1])

        