class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index):
            if index >= len(nums):
                return 0
            return max(nums[index] + dp(index + 2), dp(index + 1))
        return dp(0)
        