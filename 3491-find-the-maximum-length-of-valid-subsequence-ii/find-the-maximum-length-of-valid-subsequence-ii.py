class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        dp = [[0 for i in range(k)] for j in range(k)]
        for num in nums:
            curr = num % k
            for mod in range(k):
                prev = (mod - curr + k) % k
                dp[curr][mod] = max(dp[curr][mod], dp[prev][mod] + 1)
                ans = max(ans, dp[curr][mod])
        return ans