class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # use index as id

        nodes = {}
        edges = {}
        
        for i, account in enumerate(accounts):
            name = account[0]
            node = "%s@%d" %(name, i)
            nodes[node] = set()
            
            for j in range(1, len(account)):
                email = account[j]
                nodes[node].add(email)
                if email not in edges:
                    edges[email] = []
                edges[email].append(node)
        
        visited = set()
        merges = []
        def dfs(node, path):
            visited.add(node)
            path.append(node)
            emails = nodes[node]
            for email in emails:
                adjs = edges[email]
                for adj in adjs:
                    if adj not in visited:
                        dfs(adj,path)
        
        for node in nodes:
            if node not in visited:
                path = []
                dfs(node,path)
                merges.append(path)
        # print(merges)
        
        ret = []
        for merge in merges:
            name = merge[0].split("@")[0]
            account = [name]
            emailset = set()
            for node in merge:
                emailset = emailset.union(nodes[node])
            emaillist = list(emailset)
            emaillist.sort()
            ret.append(account + emaillist)
                
        
        return ret