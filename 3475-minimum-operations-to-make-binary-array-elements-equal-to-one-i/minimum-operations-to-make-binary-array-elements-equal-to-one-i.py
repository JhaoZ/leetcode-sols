class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                nums[i] = abs(nums[i] - 1)
                nums[i + 2] = abs(nums[i + 2] - 1)
                nums[i + 1] = abs(nums[i + 1] - 1)
                ops += 1

        return ops if sum(nums) == len(nums) else -1

        