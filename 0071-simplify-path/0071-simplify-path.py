class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        ret = []
        for path in paths:
            if path == "." or path =="":
                pass
            elif path == "..":
                if ret:
                    ret.pop()
            else:
                ret.append(path)
        if ret:
            return "/" + "/".join(ret)
        else:
            return "/"