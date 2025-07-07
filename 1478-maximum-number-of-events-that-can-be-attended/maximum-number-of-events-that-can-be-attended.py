class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events_map = defaultdict(list)
        for s, e in events:
            events_map[s].append((s, e))
        
        ans = 0
        current_day = 1
        pq = []
        keys = sorted(events_map.keys())
        keys.append(10**9)
        for i in range(len(keys) - 1):
            d = keys[i]
            for s, e in events_map[d]:
                heapq.heappush(pq, (e, s))
            
            while pq and current_day < keys[i + 1]:
                current_end, current_start = pq[0]
                if (current_day > current_end):
                    heapq.heappop(pq)
                    continue
 
                if current_start > current_day:
                    current_day = current_start + 1
                    ans += 1
                    heapq.heappop(pq)
                elif current_start <= current_day <= current_end:
                    current_day += 1
                    ans += 1
                    heapq.heappop(pq)
                else:
                    break
        return ans