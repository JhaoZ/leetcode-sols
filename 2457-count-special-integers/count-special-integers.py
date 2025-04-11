class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        
        n = str(n)

        @cache
        def dp(pos, smaller, distinct, started, mask):
            if pos >= len(n):
                return int(distinct and started)
            
            limit = 9 if smaller else int(n[pos])

            ans = 0

            for i in range(limit + 1):
                repeat = bool(mask & (1 << i))
                next_smaller = smaller or ((not smaller) and (i < int(n[pos])))
                next_started = started or (i != 0)
                next_mask = mask | (1 << i)

                if not next_started:
                    repeat = False
                    next_mask = mask
                
                ans += dp(pos + 1, next_smaller, (not repeat) and distinct, next_started, next_mask)
            
            return ans
        
        return dp(0, False, True, False, 0)
                

                
                



