class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, int(math.sqrt(n) + 1)):
            squares.append(i * i)

        @cache
        def dp(idx, curr):
            if curr == 0:
                return 0
            if idx < 0:
                return 2**31 - 1 
            
            if squares[idx] <= n:
                occur = curr // squares[idx]
                return min(dp(idx - 1, curr - (occur *squares[idx])) + occur, dp(idx - 1, curr))

            else:
                return dp(idx - 1, curr)
        
        return dp(len(squares) - 1, n)