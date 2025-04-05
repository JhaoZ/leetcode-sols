class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        inf = 2**31 - 1
        d = [[inf] * n for i in range(n)]

        for i in range(n):
            d[i][i] = 0
            if i < n - 1:
                d[i][i + 1] = 1
                d[i + 1][i] = 1
                
        if x != y:
            d[x - 1][y - 1] = 1
            d[y - 1][x - 1] = 1


        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])


        freq = Counter([d[i][j] for i in range(n) for j in range(n)])
        ans = []
        for k in range(1, n + 1):
            if k not in freq:
                ans.append(0)
            else:
                ans.append(freq[k])
        return ans