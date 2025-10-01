class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")


        for part in parts:
            if part == ".":
                pass
            elif part == "..":
                if stack:
                    stack.pop()
            elif part == "":
                pass
            else:
                stack.append(part)
        
        return "/" + "/".join(stack)