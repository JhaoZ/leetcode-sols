class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        empty_spots = [0]
        events = [[startTime[i], endTime[i]] for i in range(len(startTime))]
        prev_time = 0
        for s, e in events:
            gap = s - prev_time
            empty_spots.append(empty_spots[-1] + gap)
            prev_time = e
        if eventTime - prev_time:
            empty_spots.append(empty_spots[-1] + (eventTime - prev_time))
        
        if k >= len(empty_spots) - 1:
            return empty_spots[-1]

        ans = 0
        for i in range(k + 1, len(empty_spots)):
            ans = max(ans, empty_spots[i] - empty_spots[i - k - 1])

        return ans