class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        ret = False
        
        def dfs(i, j, m, n, word, visited):
            # print("i %d j %d word %s" %(i,j,word))
            if (i,j) in visited:
                return False
            
            if len(word) == 0:
                return True
            
            if i < 0 or j < 0 or i == m or j == n:
                return False
            

            
            visited[(i,j)] = True
            
            ret = False
            
            if i < m - 1 and board[i+1][j] == word[0]:
                ret = ret or dfs(i + 1, j, m, n, word[1:], visited.copy())
            
            if j < n -1 and board[i][j+1] == word[0]:
                ret = ret or dfs(i, j + 1, m, n, word[1:], visited.copy())
            
            if i > 0 and board[i-1][j] == word[0]:
                ret = ret or dfs(i - 1, j, m, n, word[1:], visited.copy())
            
            if j > 0 and board[i][j-1] == word[0]:
                ret = ret or dfs(i, j - 1, m, n, word[1:], visited.copy())
                
            
            return ret
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = {}
                    ret = ret or dfs(i, j, m, n, word[1:], visited)
                
     
                
        return ret
                        
                    
                        
                        