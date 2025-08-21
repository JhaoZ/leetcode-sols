from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))          # nodes are 1..n

        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        pq = [(0, k)]                     # (time, node)

        while pq:
            t, u = heapq.heappop(pq)
            if t > dist[u]:
                continue                  # stale entry
            for v, w in g[u]:
                nt = t + w
                if nt < dist[v]:          # relax
                    dist[v] = nt
                    heapq.heappush(pq, (nt, v))

        ans = max(dist.values())
        return -1 if ans == float('inf') else ans
