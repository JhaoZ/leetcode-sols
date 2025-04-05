class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def func(index, curr):
            if index == len(nums):
                return curr
            return func(index + 1, curr) + func(index + 1, curr ^ nums[index])
        return func(0, 0)