class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        @cache
        def dp(index, curr):
            if index >= len(nums):
                return curr == 0
            return dp(index + 1, curr + nums[index]) or dp(index + 1, curr - nums[index]) 
        return dp(0,0)