class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        canonical = ""
        cur = []
        dirs = [i for i in dirs if len(i)]
        for i in range(len(dirs)):
            if "." != dirs[i] and dirs[i]!='..':
                cur.append(dirs[i])
            elif dirs[i] == ".." and len(cur):
                cur.pop()
        
        for i in cur:
            canonical += "/" + i
        if not len(canonical):
            return"/"
        return canonical
            
