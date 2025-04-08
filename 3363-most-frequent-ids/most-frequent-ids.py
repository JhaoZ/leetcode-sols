class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = defaultdict(int)
        ans = [0] * len(nums)
        maxHeap = []
        for i in range(len(nums)):
            counter[nums[i]] += freq[i]
            heapq.heappush(maxHeap, (-counter[nums[i]], nums[i]))
            while counter[maxHeap[0][1]] < -maxHeap[0][0]:
                heapq.heappop(maxHeap)
            ans[i] = -maxHeap[0][0]
        return ans