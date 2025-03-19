class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        freq = Counter(nums)

        for key, val in freq.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [val for _, val in minHeap]