class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_suffix = [0] * len(nums)
        max_prefix = [0] * len(nums)
        max_prefix[0] = nums[0]
        max_suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            max_prefix[i] = max(max_prefix[i - 1], nums[i])
        for i in reversed(range(0, len(nums) - 1)):
            max_suffix[i] = max(max_suffix[i + 1], nums[i])

        ans = 0
        for j in range(1, len(nums) - 1):
            ans = max(ans, (max_prefix[j - 1] - nums[j]) * max_suffix[j + 1])
        return ans
