class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(curr):
            if curr > n:
                return
            ans.append(curr)
            for i in range(0, 10):
                temp = curr * 10 + i
                dfs(temp)

        for i in range(1, 10):
            dfs(i)
        return ans
        