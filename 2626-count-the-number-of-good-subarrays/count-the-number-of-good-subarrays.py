class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        count = 0
        freq = defaultdict(int)
        end = 0
        for start in range(len(nums)):
            while end < len(nums) and count < k:
                count += freq[nums[end]] 
                freq[nums[end]] += 1
                end += 1
            
            if count >= k:
                ans += len(nums) - (end - 1)

            freq[nums[start]] -= 1
            count -= freq[nums[start]]
        return ans
            



        