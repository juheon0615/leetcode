class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        
        for token in tokens:
            if token == "":
                continue
            elif token == ".":
                continue
            elif token == "..":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(token)
        
        ret = "/"
        for i, token in enumerate(stack):
            if i == len(stack) - 1:
                ret += token
            else:
                ret += token + "/"
        
        return ret
        