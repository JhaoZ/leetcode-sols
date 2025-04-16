class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        last_invalid, last_valid = -1, -1
        for i in range(len(nums)):
            if nums[i] > right:
                last_invalid = i
            elif nums[i] >= left:
                last_valid = i

            if nums[i] <= right:
                ans += max(0, last_valid - last_invalid)
            
        return ans