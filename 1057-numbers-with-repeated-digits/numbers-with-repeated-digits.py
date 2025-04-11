class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        n = str(n)

        @cache
        def dp(pos, smaller, started, bitmask, hasdup):
            if pos >= len(n):
                return int(hasdup)
        
            ans = 0

            if smaller:
                for i in range(0, 10):
                    seen = bool(bitmask & (1 << i)) 
                    if i == 0:
                        if started:
                            ans += dp(pos + 1, smaller, started, bitmask | (1 << i), seen or hasdup)
                        else:
                            ans += dp(pos + 1, smaller, started, bitmask, seen or hasdup)
                    else:
                        ans += dp(pos + 1, smaller, True, bitmask | (1 << i), seen or hasdup)
            else:
                for i in range(0, int(n[pos])):
                    seen = bool(bitmask & (1 << i)) 
                    if i == 0:
                        if started:
                            ans += dp(pos + 1, True, started, bitmask | (1 << i), seen or hasdup)
                        else:
                            ans += dp(pos + 1, True, started, bitmask, seen or hasdup)
                    else:
                        ans += dp(pos + 1, True, True, bitmask | (1 << i), seen or hasdup)

                seen = bool(bitmask & (1 << int(n[pos]))) 
                ans += dp(pos + 1, False, True, bitmask | (1 << int(n[pos])), seen or hasdup)
            
            return ans
        
        return dp(0, False, False, 0, False)



        