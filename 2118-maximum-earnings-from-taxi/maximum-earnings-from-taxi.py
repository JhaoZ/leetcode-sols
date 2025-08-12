class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        start_points = [start for start, _, _ in rides]
        @cache
        def dp(idx):
            if idx >= len(rides):
                return 0
            # take the passenger or not
            return max(rides[idx][1] - rides[idx][0] + rides[idx][2] + dp(bisect.bisect_left(start_points, rides[idx][1])), dp(idx + 1))
        return dp(0)
            


        