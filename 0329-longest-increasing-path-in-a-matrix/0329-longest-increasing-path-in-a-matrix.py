class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        cache = {}
        def dfs(i, j, m, n):
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            ret = 1

            moves = [[1,0], [-1, 0], [0,1], [0, -1]]

            for move in moves:
                offi, offj = move
                ii = i + offi
                jj = j + offj

                if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] > matrix[i][j]:
                    ret = max(ret, 1 + dfs(ii,jj,m,n))
            
            cache[(i,j)] = ret
            return ret
        
        m = len(matrix)
        n = len(matrix[0])

        ret = 0

        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i,j,m,n))
        # print(cache)
        return ret