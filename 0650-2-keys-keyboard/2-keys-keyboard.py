class Solution:
    def minSteps(self, n: int) -> int:

        @cache
        def dp(length, copied):
            if length == n:
                return 0
            if length > n:
                return 2**31 -1

            if copied == 0:
                return 1 + dp(length, length)
            if copied == length:
                return 1 + dp(length + copied, copied)
            else:
                return min(1 + dp(length + copied, copied), 1 + dp(length, length))
           
        return dp(1, 0)