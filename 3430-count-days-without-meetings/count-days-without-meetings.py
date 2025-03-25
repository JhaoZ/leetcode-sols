class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        merged = []
        meetings.sort(key = lambda x : x[0])

        for start, end in meetings:
            if not merged:
                merged.append([start, end])
            else:
                if start <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], end)
                else:
                    merged.append([start, end])
        merged.insert(0, [0, 0])
        merged.append([days + 1, days + 1])

        count = 0
        for i in range(1, len(merged)):
            count += (merged[i][0] - merged[i - 1][1] - 1)
        return count