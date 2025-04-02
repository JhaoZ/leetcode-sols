class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        score = weights[0] + weights[-1]
        costs_min = []
        costs_max = []

        for i in range(len(weights) - 1):
            curr_cost = weights[i] + weights[i + 1]
            heapq.heappush(costs_min, -curr_cost)
            heapq.heappush(costs_max, curr_cost)
            if len(costs_min) > k - 1:
                heapq.heappop(costs_min)
            if len(costs_max) > k - 1:
                heapq.heappop(costs_max)
        
        return (sum(costs_max)+ score) - (abs(sum(costs_min)) + score)
            
        
        