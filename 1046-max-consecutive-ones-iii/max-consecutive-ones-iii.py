class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        right = 0
        zero_counter = 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_counter += 1
            
            if zero_counter <= k:
                ans = max(ans, right - left + 1)

            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1
                if zero_counter <= k:
                    ans = max(ans, right - left + 1)
            right += 1
        return ans


        