class Solution:
    def countDigitOne(self, n: int) -> int:

        n = str(n)

        @cache
        def dp(pos, smaller, cnt):
            if pos >= len(n):
                return cnt
            
            ans = 0

            if smaller:
                for i in range(0, 10): 
                    if i == 1:
                        ans += dp(pos + 1, smaller, cnt + 1)
                    else:
                        ans += dp(pos + 1, smaller, cnt)
            else:
                for i in range(0, int(n[pos])):
                    if i == 1:
                        ans += dp(pos + 1, True, cnt + 1)
                    else:
                        ans += dp(pos + 1, True, cnt)                                
                if int(n[pos]) == 1:
                    ans += dp(pos + 1, False, cnt + 1)
                else:
                    ans += dp(pos + 1, False, cnt)
            return ans
        
        return dp(0, False, 0) 
        