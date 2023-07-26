class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        path = []
        its = {}
        for src,dst in tickets:
            if src not in its:
                its[src] = []
            
            its[src].append(dst)
        
        for src in its:
            its[src].sort()
        
        
        
        def dfs(city):
            while city in its and its[city]:
                dst = its[city].pop(0)
                dfs(dst)
            
            path.append(city)

        dfs("JFK")
        return path[::-1]