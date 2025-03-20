class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for a in arr:
            if a == "":
                continue
            if a == "..":
                if stack:
                    stack.pop()
            elif a == ".":
                continue
            else:
                stack.append(a)
        ans = '/'
        for i in stack:
            ans += i
            ans += '/'
        
        return ans[:-1] if len(ans) > 1 else ans
        