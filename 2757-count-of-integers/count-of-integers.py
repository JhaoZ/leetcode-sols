class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(curr, pos, smaller, digit_sum):

            if digit_sum > max_sum:
                return 0

            if pos >= len(curr):
                return int(min_sum <= digit_sum <= max_sum)

            
            res = 0
            if not smaller:
                for i in range(0, int(curr[pos])):
                    res = (res + dp(curr, pos + 1, True, i + digit_sum))
                res = (res + dp(curr, pos + 1, False, digit_sum + int(curr[pos])))
            else:
                for i in range(0, 10):
                    res = (res + dp(curr, pos + 1, smaller, i + digit_sum)) 
            return res % MOD
        
        return (dp(num2, 0, False, 0) - dp(str(int(num1) - 1), 0, False, 0) + MOD) % MOD

            
