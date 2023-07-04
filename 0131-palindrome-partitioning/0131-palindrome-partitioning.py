class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
        
            for i in range(len(s)):
                ss = s[:i+1]
                
                if ss == ss[::-1]:
                    path.append(s[:i+1])
                    dfs(s[i+1:], path, res)
                    path.pop()
        
        res = [] 
        dfs(s, [], res)
        return res
        
                
                
        