class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        start_times = [s for s, _, _ in events]

        @cache
        def dp(idx, curr_k):
            if idx >= len(events):
                return 0
            if curr_k <= 0:
                return 0
            
            start, end, points = events[idx]
            next_event_idx = bisect.bisect_left(start_times, end + 1)

            return max(dp(idx + 1, curr_k), points + dp(next_event_idx, curr_k - 1))
        
        return dp(0, k)




