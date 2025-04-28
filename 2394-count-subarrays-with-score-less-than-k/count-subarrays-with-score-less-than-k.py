class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0

        start = 0
        running = 0
        for end in range(len(nums)):
            while start < len(nums) and running * (start - end) < k:
                running += nums[start]
                start += 1
            
            if running * (start - end) >= k:
                cnt += len(nums) - (start - 1)
            
            running -= nums[end]
        n = len(nums)
        return (((n * (n - 1)) // 2) + n)- cnt
            

        