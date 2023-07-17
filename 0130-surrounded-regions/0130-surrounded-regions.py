class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for __ in range(m)]
        
        q = []
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == "O":
                    q.append((i,j))
                    visited[i][j] = True                                      
                                    
        qi = 0

        while qi < len(q):
            qlen = len(q)

            for qii in range(qi, qlen):
                i,j = q[qii]

                visited[i][j] = True

                # down
                if i < m - 1 and visited[i+1][j] == False and board[i+1][j] == "O":
                    q.append((i+1, j))
                # up
                if i > 0 and visited[i-1][j] == False and board[i-1][j] == "O":
                    q.append((i-1, j))

                # left
                if j > 0 and visited[i][j-1] == False and board[i][j-1] == "O":
                    q.append((i, j-1))

                # right
                if j < n - 1 and visited[i][j+1] == False and board[i][j+1] == "O":
                    q.append((i, j+1))

            qi = qlen
                        


        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and board[i][j] == "O":
                    board[i][j] = "X"
        
        
        