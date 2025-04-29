class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ele = max(nums)
        start = 0
        freq = 0
        ans = 0
        for end, num in enumerate(nums):
            if num == ele:
                freq += 1
            while freq == k:
                if nums[start] == ele:
                    freq -= 1
                start += 1
            ans += start
        return ans