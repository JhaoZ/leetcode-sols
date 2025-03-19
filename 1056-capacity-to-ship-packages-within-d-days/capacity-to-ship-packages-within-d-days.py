class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        
        def works(capacity):
            days_needed = 1
            curr = 0
            for w in weights:
                if w + curr > capacity: 
                    days_needed += 1
                    curr = w
                else:
                    curr += w

            return days_needed <= days
        
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = l + (r - l) // 2
            if works(mid):
                r = mid
            else:
                l = mid + 1
        return r
        